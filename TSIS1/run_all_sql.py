from connect import connect

conn = connect()
cur = conn.cursor()

for filename in ["schema.sql", "procedures.sql"]:
    with open(filename, "r", encoding="utf-8") as f:
        cur.execute(f.read())
    print(filename, "loaded")

conn.commit()
cur.close()
conn.close()

print("Database is ready!")