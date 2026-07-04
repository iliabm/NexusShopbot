import sqlite3

conn = sqlite3.connect("nexus.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    language TEXT DEFAULT 'fa'
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT,
    quantity INTEGER,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()

def add_user(user_id, language="fa"):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, language) VALUES (?, ?)",
        (user_id, language)
    )
    conn.commit()

def create_order(user_id, product, quantity):
    cursor.execute(
        "INSERT INTO orders (user_id, product, quantity) VALUES (?, ?, ?)",
        (user_id, product, quantity)
    )
    conn.commit()

def get_orders():
    cursor.execute("SELECT * FROM orders")
    return cursor.fetchall()
