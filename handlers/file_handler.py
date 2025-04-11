# فایل: handlers/file_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from database.queries import is_user_registered, save_file_info


# فقط کاربران ثبت‌نام‌شده اجازه ارسال فایل دارند
ALLOWED_EXTENSIONS = {".stl", ".rar", ".zip", ".3dm"}


def get_file_extension(filename: str) -> str:
    for ext in ALLOWED_EXTENSIONS:
        if filename.lower().endswith(ext):
            return ext
    return ""


async def file_receiver_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📥 فایل جدید دریافت شد از:" )
    user = update.effective_user
    telegram_id = user.id

    # چک کردن عضویت
    if not is_user_registered(telegram_id):
        await update.message.reply_text("❗ فقط کاربران عضو شده می‌توانند فایل ارسال کنند.")
        return

    document = update.message.document
    if not document:
        return

    filename = document.file_name
    ext = get_file_extension(filename)

    if ext == "":
        await update.message.reply_text("❌ فرمت فایل مجاز نیست. فرمت‌های مجاز: STL, RAR, ZIP, 3DM")
        return

    file_id = document.file_id
    file_unique_id = document.file_unique_id

    # ذخیره در دیتابیس
    save_file_info(
        telegram_id=telegram_id,
        file_id=file_id,
        file_unique_id=file_unique_id,
        file_name=filename,
        file_type=ext
    )

    await update.message.reply_text(f"📁 فایل «{filename}» با موفقیت ثبت شد ✅")
