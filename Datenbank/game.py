import sqlite3
def login(username, password):
    username = input("username: ")
    password = input("password: ")
    check(username, password)

def check(username, password):
    conn = sqlite3.connect('tier.db')
    cur = conn.cursor()

username = None
password = None