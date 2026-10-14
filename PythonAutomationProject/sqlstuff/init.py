import sqlite3

conn = sqlite3.connect("ElDataBase.db")
cur = conn.cursor()


def makeEntry(username, password):
    cur.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    print("Success")

def initDB():
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        username TEXT,
        password TEXT
    )
    ''')
