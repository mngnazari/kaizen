import sqlite3
from datetime import datetime
from database.db import get_connection

# بررسی عضویت کاربر
def is_user_registered(telegram_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# ⏺ ذخیره اطلاعات فایل - و برگرداندن شناسه ردیف
def save_file_info(
    telegram_id: int,
    file_id: str,
    file_unique_id: str,
    file_name: str,
    file_type: str,
    status: str = "جدید",
    quantity: int = 1,
    description: str = "فاقد توضیحات",
    preview_file_id: str = "",
    delivery_date: str = ""
) -> int:
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
        quantity,
        description,
        delivery_date,
        status,
        preview_file_id
    ))

    file_db_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return file_db_id

# 🔍 بازیابی اطلاعات فایل با id
def get_file_data_by_id(file_db_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT file_name, file_type, quantity, description, delivery_time, file_id
        FROM files
        WHERE id = ?
    """, (file_db_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "file_name": row[0],
            "file_type": row[1],
            "quantity": row[2],
            "description": row[3],
            "delivery_time": row[4],
            "file_id": row[5],
        }
    return None

# ✏️ به‌روزرسانی توضیحات با id فایل
def update_description_by_id(file_db_id: int, new_description: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE files SET description = ? WHERE id = ?
    """, (new_description, file_db_id))
    conn.commit()
    conn.close()

# 🔢 به‌روزرسانی تعداد فایل با id
def update_quantity_by_id(file_db_id: int, new_quantity: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE files SET quantity = ? WHERE id = ?
    """, (new_quantity, file_db_id))
    conn.commit()
    conn.close()
