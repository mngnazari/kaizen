import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "kaizen.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

# بررسی عضویت کاربر
def is_registered_user(telegram_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,))
        return cursor.fetchone() is not None

# بررسی اینکه کاربر ادمین است یا نه
def is_admin(telegram_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE telegram_id = ?", (telegram_id,))
        row = cursor.fetchone()
        return row and row[0] == "admin"

# بررسی اینکه کاربر اپراتور است یا نه
def is_operator(telegram_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE telegram_id = ?", (telegram_id,))
        row = cursor.fetchone()
        return row and row[0] == "operator"

# بررسی اینکه کاربر مشتری است یا نه
def is_customer(telegram_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE telegram_id = ?", (telegram_id,))
        row = cursor.fetchone()
        return row and row[0] == "customer"
