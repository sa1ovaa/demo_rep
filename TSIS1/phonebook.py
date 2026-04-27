import csv
import json
import os
from datetime import date, datetime

import psycopg2
import psycopg2.extras
from connect import get_connection


def _conn():
    return get_connection()


def _fmt_date(d):
    return d.isoformat() if d else "—"


def _parse_date(value):
    value = (value or "").strip()
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return None


def _get_ids(query, params=()):
    with _conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, params)
            return [row["id"] for row in cur.fetchall()]


def _fetch_contacts(ids):
    if not ids:
        return []

    with _conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                SELECT c.id, c.first_name, c.last_name, c.email,
                       c.birthday, g.name AS group_name
                FROM contacts c
                LEFT JOIN groups g ON g.id = c.group_id
                WHERE c.id = ANY(%s)
                """,
                (ids,)
            )
            contacts = {r["id"]: dict(r) for r in cur.fetchall()}

            cur.execute(
                "SELECT contact_id, phone, type FROM phones WHERE contact_id = ANY(%s)",
                (ids,)
            )
            for row in cur.fetchall():
                contacts[row["contact_id"]].setdefault("phones", []).append(
                    {"phone": row["phone"], "type": row["type"]}
                )

    return [contacts[i] for i in ids if i in contacts]


def _show_contacts(ids):
    rows = _fetch_contacts(ids)
    if not rows:
        print("No contacts found")
        return

    for r in rows:
        phones = ", ".join(
            f"{p['phone']} [{p['type']}]" for p in r.get("phones", [])
        ) or "No phones"

        print(f"\n[{r['id']}] {r['first_name']} {r.get('last_name') or ''}")
        print(f"Email: {r.get('email') or '—'}")
        print(f"Birthday: {_fmt_date(r.get('birthday'))}")
        print(f"Group: {r.get('group_name') or '—'}")
        print(f"Phones: {phones}")


def search_by_email():
    email = input("Email search: ").strip().lower()
    ids = _get_ids(
        "SELECT id FROM contacts WHERE LOWER(email) LIKE %s",
        (f"%{email}%",)
    )
    _show_contacts(ids)


def filter_by_group():
    group = input("Group name: ").strip()
    ids = _get_ids(
        """
        SELECT c.id
        FROM contacts c
        JOIN groups g ON g.id = c.group_id
        WHERE LOWER(g.name) = LOWER(%s)
        """,
        (group,)
    )
    _show_contacts(ids)


def export_json():
    ids = _get_ids("SELECT id FROM contacts ORDER BY first_name")
    rows = _fetch_contacts(ids)

    for r in rows:
        if isinstance(r.get("birthday"), date):
            r["birthday"] = r["birthday"].isoformat()

    with open("contacts_export.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    print("Export completed")


def add_phone():
    name = input("Contact first name: ").strip()
    phone = input("Phone: ").strip()
    ptype = input("Type (home/work/mobile): ").strip() or "mobile"

    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        conn.commit()

    print("Phone added")


def move_to_group():
    name = input("Contact first name: ").strip()
    group = input("New group: ").strip()

    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
        conn.commit()

    print("Contact moved")


def search_all():
    text = input("Search: ").strip()

    with _conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (text,))
            ids = [r["id"] for r in cur.fetchall()]

    _show_contacts(ids)


MENU = """
1. Search by email
2. Filter by group
3. Export to JSON
4. Add phone
5. Move to group
6. Search all fields
Q. Quit
"""


HANDLERS = {
    "1": search_by_email,
    "2": filter_by_group,
    "3": export_json,
    "4": add_phone,
    "5": move_to_group,
    "6": search_all,
}


def main():
    while True:
        print(MENU)
        choice = input("Choose: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        func = HANDLERS.get(choice)
        if func:
            try:
                func()
            except psycopg2.Error as e:
                print("Database error:", e)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()