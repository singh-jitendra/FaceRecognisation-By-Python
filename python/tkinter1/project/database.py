import sqlite3

def connect():
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS regis (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, USER_NAME TEXT,PASSWORD INTEGER,D_O_B DATE, GENDER TEXT)")
    conn.commit()
    conn.close()

def connect1():
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS face_name (name text)")
    conn.commit()
    conn.close()

def connect2():
    conn = sqlite3.connect("face.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS subject (name text)")
    conn.commit()
    conn.close()


def insert(NAME,USER_NAME,PASSWORD,D_O_B,GENDER):
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO regis VALUES (NULL,?,?,?,?,?)",(NAME,USER_NAME,PASSWORD,D_O_B,GENDER))
    conn.commit()
    conn.close()
    view()

def insert1(face_name):
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO face_name VALUES (?)",(face_name,))
    conn.commit()
    conn.close()
    view()

def insert2(sub_name):
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO subject VALUES (?)",(sub_name,))
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM regis")
    rows=cur.fetchall()
    conn.close()
    return rows

def view1():
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM face_name")
    rows=cur.fetchall()
    conn.close()
    return rows
def view2():
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM subject")
    rows=cur.fetchall()
    conn.close()
    return rows



def search(USER_NAME):
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("SELECT PASSWORD, NAME FROM regis WHERE USER_NAME=(?) ", (USER_NAME,))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete():
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM face_name")
    conn.commit()
    conn.close()

def delete1():
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM subject")
    conn.commit()
    conn.close()


def update(ID,NAME,USER_NAME,PASSWORD,GENDER):
    conn=sqlite3.connect("face.db")
    cur=conn.cursor()
    cur.execute("UPDATE regis SET NAME=?, USER_NAME=?, PASSWORD=?, GENDER=? WHERE ID=?",(NAME,USER_NAME,PASSWORD,GENDER,ID))
    conn.commit()
    conn.close()

connect()
connect1()
connect2()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(USER_NAME="John Smooth"))
