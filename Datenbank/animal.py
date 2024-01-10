def create():
    cur.execute('''CREATE TABLE IF NOT EXISTS tier 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                tiername TEXT NOT NULL, 
                art TEXT NOT NULL, 
                age INTEGER NOT NULL)''')

def add(name, art, age):
    cur.execute("insert into tier(tiername, art, age) values (?,?,?)", (name, art, age))
    conn.commit()

def show():
    cur.execute("select * from tier")
    rows = cur.fetchall()
    print(rows)

def delete(id):
    cur.execute("delete from tier where id = ?",(id))
    conn.commit()

def update(id):
    name = 'Fiffy'
    cur.execute("update tier set tiername = ? where id = ?", (name, id))
    conn.commit()

import sqlite3
conn = sqlite3.connect('tier.db')
cur = conn.cursor()

show()