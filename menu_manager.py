from telegram import Update
from telegram.ext import ContextTypes
from menus import menus


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_where="msg"):
    text = update.message.text  # فقط پیام متنی واقعی، نه else 'start'

    # اگر متن واردشده توی منو نیست، بی‌خیال شو یا یه پیام بده
    current_menu = context.user_data.get("current_menu", "main_customer")
    menu = menus.get(current_menu, {})

    handler = menu.get(text)

    if handler:
        await handler(update, context)
    else:
        await update.message.reply_text("❗ گزینه نامعتبر است یا هنوز پیاده‌سازی نشده.")
