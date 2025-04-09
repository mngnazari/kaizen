from telegram import Update
from telegram.ext import ContextTypes
from menus import menu_map


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_where="msg"):
    # 🔘 گرفتن متن دکمه فشرده‌شده یا پیام کاربر
    text = update.message.text if from_where == "msg" else update.callback_query.data

    # 📍 منوی فعلی را از user_data بخوان
    current_menu = context.user_data.get("current_menu", "main_customer")
    menu = menu_map.get(current_menu, {})

    # 🔍 پیدا کردن تابع مرتبط با دکمه
    handler = menu.get(text)

    # ⬆️ اگر دکمه بازگشت باشد (UP)، اجرای تابع برگشت به منوی والد
    if handler == "UP":
        from handlers.common import up_menu
        await up_menu(update, context)
        return

    # ✅ اگر handler یک تابع باشد، آن را اجرا کن
    if callable(handler):
        await handler(update, context)

    # ❌ اگر handler تعریف نشده بود یا نامعتبر بود
    else:
        await update.message.reply_text("❗ گزینه نامعتبر است یا هنوز پیاده‌سازی نشده.")
