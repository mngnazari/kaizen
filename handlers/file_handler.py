from telegram import Update
from telegram.ext import ContextTypes
from database.queries import save_file_info, get_file_data_by_id
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
    document = update.message.document

    if not document:
        return

    filename = document.file_name
    ext = get_file_extension(filename)
    if not ext:
        await update.message.reply_text("❌ فرمت فایل مجاز نیست.")
        return

    file_id = document.file_id
    file_unique_id = document.file_unique_id

    file_db_id = save_file_info(
        telegram_id=telegram_id,
        file_id=file_id,
        file_unique_id=file_unique_id,
        file_name=filename,
        file_type=ext,
        quantity=1
    )

    file_data = get_file_data_by_id(file_db_id)
    if not file_data:
        await update.message.reply_text("❗ خطا در دریافت اطلاعات فایل.")
        return

    caption = (
        f"📦 فایل: {file_data['file_name']}\n"
        f"🕒 زمان تحویل: {file_data['delivery_time'] or '—'}\n"
        f"🔢 تعداد: {file_data['quantity']}\n"
        f"📝 توضیحات: {file_data['description'] or '—'}"
    )

    # ذخیره مقدار quantity خاص برای این فایل
    context.user_data[f"quantity_{file_db_id}"] = file_data["quantity"]
    context.user_data["file_db_id"] = file_db_id

    sent_message = await update.message.reply_document(
        file_data["file_id"],
        caption=caption,
        reply_markup=build_inline_keyboard("file_action_menu", context, file_db_id)
    )

    # ذخیره پیام برای ویرایش بعدی
    context.user_data[f"file_msg_{file_db_id}"] = {
        "chat_id": update.effective_chat.id,
        "message_id": sent_message.message_id
    }
