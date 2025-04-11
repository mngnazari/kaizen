from telegram import Update, InputFile
from telegram.ext import ContextTypes
from database.queries import is_user_registered, save_file_info, get_file_data_by_unique_id
from handlers.inline.keyboards import build_inline_keyboard

ALLOWED_EXTENSIONS = {".stl", ".rar", ".zip", ".3dm"}


def get_file_extension(filename: str) -> str:
    for ext in ALLOWED_EXTENSIONS:
        if filename.lower().endswith(ext):
            return ext
    return ""


async def file_receiver_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_id = user.id

    # 🛡 بررسی ثبت‌نام
    if not is_user_registered(telegram_id):
        await update.message.reply_text("❗ فقط کاربران عضو شده می‌توانند فایل ارسال کنند.")
        return

    document = update.message.document
    if not document:
        return

    filename = document.file_name
    ext = get_file_extension(filename)

    if ext == "":
        await update.message.reply_text("❌ فرمت فایل مجاز نیست. مجاز: STL, RAR, ZIP, 3DM")
        return

    file_id = document.file_id
    file_unique_id = document.file_unique_id

    # ✅ ذخیره در دیتابیس
    save_file_info(
        telegram_id=telegram_id,
        file_id=file_id,
        file_unique_id=file_unique_id,
        file_name=filename,
        file_type=ext
    )

    # 🎯 بارگذاری اطلاعات فایل از دیتابیس
    file_data = get_file_data_by_unique_id(file_unique_id)
    if not file_data:
        await update.message.reply_text("⚠️ مشکلی در بازیابی فایل از دیتابیس پیش آمد.")
        return

    # 💾 ذخیره اطلاعات فایل در user_data
    context.user_data["inline_current_menu"] = "file_action_menu"
    context.user_data["inline_file_unique_id"] = file_unique_id
    context.user_data["file_quantity"] = file_data["quantity"]  # ← مقداردهی جداگانه هر فایل

    # 📝 ساخت کپشن فایل
    caption = (
        f"📦 فایل: {file_data['file_name']}\n"
        f"🕒 زمان تحویل: {file_data['delivery_time'] or '—'}\n"
        f"🔢 تعداد: {file_data['quantity']}\n"
        f"📝 توضیحات: {file_data['description']}"
    )

    # ⌨ ارسال فایل با کیبورد شیشه‌ای
    await update.message.reply_document(
        document=file_id,
        caption=caption,
        reply_markup=build_inline_keyboard("file_action_menu", context)
    )
