import sqlite3
class animal:
    conn = sqlite3.connect('tier.db')
    cur = conn.cursor()

    def __init__(self):
        conn = sqlite3.connect('tier.db')
        cur = conn.cursor()

    def create(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS tier 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    tiername TEXT NOT NULL, 
                    art TEXT NOT NULL, 
                    age INTEGER NOT NULL)''')

    def add(self, name, art, age):
        self.cur.execute("insert into tier(tiername, art, age) values (?,?,?)", (name, art, age))
        self.conn.commit()

    def show(self):
        self.cur.execute("select * from tier")
        rows = self.cur.fetchall()
        print(rows)

    def delete(self, id):
        self.cur.execute("delete from tier where id = ?",(id))
        self.conn.commit()

    def update(self, id):
        name = 'Fiffy'
        self.cur.execute("update tier set tiername = ? where id = ?", (name, id))
        self.conn.commit()