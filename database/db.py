import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "kaizen.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    if not DB_PATH.exists():
        print("🛠 در حال ایجاد دیتابیس جدید...")
        with get_connection() as conn:
            with open(SCHEMA_PATH, encoding="utf-8") as f:
                conn.executescript(f.read())
        print("✅ دیتابیس با موفقیت ساخته شد.")
    else:
        print("📦 دیتابیس از قبل وجود دارد.")

def save_user_to_db(telegram_id, full_name, phone, address, inviter_id=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO users (telegram_id, full_name, phone, address, inviter_id)
        VALUES (?, ?, ?, ?, ?)
    """, (telegram_id, full_name, phone, address, inviter_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
