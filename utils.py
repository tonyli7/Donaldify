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
    c.execute('insert into post values("'+username+'","'+title+'","'+content+'")')
    conn.commit()

Post('dar','ge','gerhtrjrt')
c = getAllPosts()
print (c)









