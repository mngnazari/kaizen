from telegram import Update
from telegram.ext import ContextTypes
from menus import menu_map


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_where="msg"):
    # گرفتن متن انتخاب‌شده توسط کاربر (چه از دکمه ثابت، چه پیام)
    text = update.message.text if from_where == "msg" else update.callback_query.data

    # گرفتن منوی فعلی از user_data
    current_menu = context.user_data.get("current_menu", "main_customer")
    menu = menu_map.get(current_menu, {})

    # اجرای تابع مرتبط با دکمه
    handler = menu.get(text)

    if handler:
        await handler(update, context)
    else:
        await update.message.reply_text("❗ گزینه نامعتبر است یا هنوز پیاده‌سازی نشده.")
