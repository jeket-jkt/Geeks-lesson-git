import sqlite3

def get_connection():
    return sqlite3.connect("vehicles.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            brand TEXT,
            model TEXT,
            year INTEGER,
            seats INTEGER,
            has_sidecar BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()