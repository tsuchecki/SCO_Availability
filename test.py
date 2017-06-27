import sqlite3

def connection():
    conn=sqlite3.connect("D:\Documents\RETAIL MONITORING\logs\lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dane (data INTEGER, status TEXT, wartosc INTEGER)")
    conn.commit()
    conn.close()

def insert(data, status, wartosc):
    conn=sqlite3.connect("D:\Documents\RETAIL MONITORING\logs\lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO dane VALUES(?,?,?)", (data, status, wartosc))
    conn.commit()
    conn.close()

with open(r"D:\Documents\RETAIL MONITORING\logs\scotapp.stf", 'r') as file:
    insert(file.readlines())


def view():
    conn=sqlite3.connect("D:\Documents\RETAIL MONITORING\logs\lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM dane")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
