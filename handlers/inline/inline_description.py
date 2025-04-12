from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from database.queries import update_description_by_id, get_file_data_by_id
from handlers.inline.keyboards import build_inline_keyboard

async def description_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_db_id = context.user_data.get("awaiting_description_file_id")
    if not file_db_id:
        return

    description = update.message.text
    update_description_by_id(file_db_id, description)
    context.user_data["awaiting_description_file_id"] = None

    file_data = get_file_data_by_id(file_db_id)
    if not file_data:
        await update.message.reply_text("❗ خطا در بروزرسانی توضیحات.")
        return

    caption = (
        f"📦 فایل: {file_data['file_name']}\n"
        f"🕒 زمان تحویل: {file_data['delivery_time'] or '—'}\n"
        f"🔢 تعداد: {file_data['quantity']}\n"
        f"📝 توضیحات: {file_data['description'] or '—'}"
    )

    msg_info = context.user_data.get(f"file_msg_{file_db_id}")
    if msg_info:
        try:
            await context.bot.edit_message_caption(
                chat_id=msg_info["chat_id"],
                message_id=msg_info["message_id"],
                caption=caption,
                parse_mode=ParseMode.HTML,
                reply_markup=build_inline_keyboard("file_action_menu", context, file_db_id)
            )
            await update.message.reply_text("✅ توضیحات ذخیره شد.")
        except Exception as e:
            print("❗ خطا در ارسال مجدد فایل:", e)
            await update.message.reply_text("⚠️ توضیحات ذخیره شد ولی ارسال فایل مجدد انجام نشد.")
