import sqlite3 as sql
from datetime import datetime
def create_table():
    conn = sql.connect("face_log.db")
    cusor = conn.cursor()

    cusor.execute("""CREATE TABLE IF NOT EXISTS user_faces(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT,
                date TEXT)
                  
                  """)

    conn.commit()
    conn.close()


def insert_data(name):
    conn = sql.connect("face_log.db")
    cusor = conn.cursor()

    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%Y-%m-%d")

    cusor.execute("INSERT INTO user_faces (name, time, date) VALUES (?, ?, ?)", (name, time, date))

    conn.commit()
    conn.close()

last_seen = {}
def can_log(name):
    now = datetime.now()
    if name not in last_seen:
        last_seen[name] = now
        return True
    diff = (now - last_seen[name]).seconds
    if diff > 30:
        last_seen[name] = now
        return True
    return False
