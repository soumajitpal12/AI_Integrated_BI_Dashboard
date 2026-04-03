import sqlite3
import hashlib


def create_user_table():

    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):

    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()

    hashed = hash_password(password)

    try:

        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, hashed)
        )

        conn.commit()
        conn.close()

        return True

    except:

        conn.close()
        return False


def login_user(username, password):

    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )

    result = cursor.fetchone()

    conn.close()

    return result