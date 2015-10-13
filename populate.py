import sqlite3

conn = sqlite3.connect('bloginator.db')
c = conn.cursor()

q = 'INSERT INTO post VALUES ("darwin", "first post", "testing")'
c.execute(q)

q = 'INSERT INTO post VALUES ("darwin", "eoitbj", "hi")'
c.execute(q)

conn.commit()
