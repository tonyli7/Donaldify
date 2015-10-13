import sqlite3

#conn = sqlite3.connect('bloginator.db')
#c = conn.cursor()

def edit(user, title, new_content):
    conn = sqlite3.connect('bloginator.db')
    c = conn.cursor()
    q = """
    UPDATE post
    SET content='""" + new_content +"""'
    WHERE user='""" + user + """'
    AND title='""" + title + "'"
    c.execute(q)
    conn.commit()
    conn.close()

def delete(user, title):
    conn = sqlite3.connect('bloginator.db')
    c = conn.cursor()
    q = """
    DELETE FROM post
    WHERE user='"""+ user """'
    AND title='"""+ title + "'"
    c.execute(q)
    conn.commit()
    conn.close()

