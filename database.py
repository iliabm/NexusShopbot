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
def add_order(user_id, product):
    cursor.execute(
        "INSERT INTO orders (user_id, product, quantity) VALUES (?, ?, ?)",
        (user_id, product, 1)
    )
    conn.commit()


def get_user_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


def get_order_count():
    cursor.execute("SELECT COUNT(*) FROM orders")
    return cursor.fetchone()[0]


def get_user_language(user_id):
    cursor.execute(
        "SELECT language FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return "fa"


def set_user_language(user_id, language):
    cursor.execute(
        "UPDATE users SET language=? WHERE user_id=?",
        (language, user_id)
    )

    conn.commit()


def update_order_status(order_id, status):
    cursor.execute(
        "UPDATE orders SET status=? WHERE id=?",
        (status, order_id)
    )

    conn.commit()
