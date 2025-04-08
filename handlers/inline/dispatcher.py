from telegram import Update
from telegram.ext import ContextTypes
from . import actions

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data  # مثل preview:FILE123
    if ":" in data:
        action, payload = data.split(":", 1)
    else:
        action, payload = data, ""

    # فراخوانی تابع از فایل actions
    handler = getattr(actions, action, None)
    if handler:
        await handler(update, context, payload)
    else:
        await query.edit_message_text("❗ دستور نامعتبر است.")
