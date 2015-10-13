import sqlite3

conn = sqlite3.connect("bloginator.db")

c = conn.cursor()

q = "CREATE TABLE post(user text, title text, content text)"
c.execute(q)

conn.commit()
conn.close()
