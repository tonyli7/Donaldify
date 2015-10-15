# Utilities File

import sqlite3

# Put misc functions such as login authentication here
def loginauth(un,pw):
    if un=="HERES" and pw=="JOHNNY":
        return True;
    else:
        return False;

# Maybe something for inserting a new UN/PW combo from register too

def getAllPosts():
    conn = sqlite3.connect('bloginator.db')
    c = conn.cursor()
    c.execute('select * from post;')
    return c.fetchall()

def Post(username,title,content):
    conn = sqlite3.connect('bloginator.db')
    c = conn.cursor()
    r = c.execute('select * from post where title = "'+title+'"')
    for i in r:
        return False
    c.execute('insert into post values("'+username+'","'+title+'","'+content+'")')
    conn.commit()

def getPost(title):
    conn = sqlite3.connect('bloginator.db')
    c = conn.cursor()
    c.execute('select * from post where title = "'+title+'"')
    return c.fetchall()

#how to read post table, for loop, index 0 is user, 1 is title, 2 is content

def edit(user, title, new_content):
    conn = sqlite3.connect('bloginator.db')
    c = conn.cursor()
    q = """
    UPDATE post
    SET content="' + new_content +'"
    WHERE user="'+ user + '"
    AND title="'+ title + '"
    """
    c.execute(q)
    conn.commit()
    conn.close()
    
def delete(user, title):
    conn = sqlite3.connect('bloginator.db')
    c = conn.cursor()
    q = """
    DELETE FROM post
    WHERE user="'+ user +'"
    AND title="'+ title +'" 
    """
    c.execute(q)
    conn.commit()
    conn.close()
