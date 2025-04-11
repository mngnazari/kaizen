import sqlite3
from datetime import datetime
from .db import get_connection


# ✅ بررسی ثبت‌نام بودن کاربر
def is_user_registered(telegram_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


# ✅ ذخیره اطلاعات فایل دریافتی
def save_file_info(
    telegram_id: int,
    file_id: str,
    file_unique_id: str,
    file_name: str,
    file_type: str,
    status: str = "در انتظار بررسی",
    quantity: int = 1,
    description: str = "فاقد توضیحات",
    preview_file_id: str = None,
    delivery_date: str = None
):
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat(timespec="seconds")

    cursor.execute("""
        INSERT INTO files (
            telegram_id,
            file_name,
            file_type,
            file_id,
            file_unique_id,
            sent_at,
            quantity,
            description,
            delivery_time,
            file_status,
            preview_file_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        telegram_id,
        file_name,
        file_type,
        file_id,
        file_unique_id,
        timestamp,
        1,  # quantity (پیش‌فرض)
        "فاقد توضیحات",  # description
        "",  # delivery_time
        "جدید",  # ✅ file_status (درست شد)
        ""  # preview_file_id
    ))

    conn.commit()
    conn.close()

