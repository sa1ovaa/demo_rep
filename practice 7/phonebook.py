import psycopg2
import csv

DB_PARAMS = {
    "host": "localhost",
    "database": "phonebook_db",
    "user": "postgres",
    "password": "Aruzhan2007",  
    "port": "5432"
}

def run_query(sql, params=None, is_select=False):
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute(sql, params)
        result = cur.fetchall() if is_select else None
        conn.commit()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print("Ошибка:", e)

# 1. Создание таблицы
def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """
    run_query(sql)

# 2. Вставка вручную
def insert_manual():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    run_query(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    print("Контакт добавлен!")

# 3. Вставка из CSV
def insert_from_csv(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, phone = row
                run_query(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )
        print("CSV данные загружены!")
    except Exception as e:
        print("Ошибка CSV:", e)

# 4. Показать все
def show_contacts():
    rows = run_query("SELECT * FROM phonebook", is_select=True)
    print("\nТелефонная книга:")
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]}")

# 5. Поиск по имени
def find_by_name():
    name = input("Введите имя: ")
    rows = run_query(
        "SELECT * FROM phonebook WHERE name = %s",
        (name,),
        True
    )
    for r in rows:
        print(r)

# 6. Поиск по телефону
def find_by_phone():
    phone = input("Введите телефон: ")
    rows = run_query(
        "SELECT * FROM phonebook WHERE phone = %s",
        (phone,),
        True
    )
    for r in rows:
        print(r)

# 7. Обновление телефона
def update_phone():
    name = input("Имя: ")
    new_phone = input("Новый телефон: ")
    run_query(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )
    print("Телефон обновлен!")

# 8. Обновление имени
def update_name():
    old_name = input("Старое имя: ")
    new_name = input("Новое имя: ")
    run_query(
        "UPDATE phonebook SET name = %s WHERE name = %s",
        (new_name, old_name)
    )
    print("Имя обновлено!")

# 9. Удаление
def delete_contact():
    name = input("Введите имя для удаления: ")
    run_query(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )
    print("Контакт удален!")

# 10. Меню
def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Добавить контакт (вручную)")
        print("2. Загрузить из CSV")
        print("3. Показать все")
        print("4. Найти по имени")
        print("5. Найти по телефону")
        print("6. Обновить телефон")
        print("7. Обновить имя")
        print("8. Удалить контакт")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            insert_manual()
        elif choice == "2":
            insert_from_csv("data.csv")
        elif choice == "3":
            show_contacts()
        elif choice == "4":
            find_by_name()
        elif choice == "5":
            find_by_phone()
        elif choice == "6":
            update_phone()
        elif choice == "7":
            update_name()
        elif choice == "8":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Неверный ввод!")

# ЗАПУСК
if __name__ == "__main__":
    create_table()
    menu()