from connect import connect

conn = connect()
cur = conn.cursor()

with open("procedures.sql", "r", encoding="utf-8") as f:
    sql = f.read()

cur.execute(sql)

conn.commit()
cur.close()
conn.close()

print("Procedures loaded!")