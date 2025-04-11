# فایل: main.py

from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from menu_manager import handle_menu
from handlers.start import start_handler  # ← هندلر جدید و استاندارد start
from handlers.inline.inline_menu_manager import handle_callback_query
from handlers.register import registration_conversation
from handlers.file_handler import file_receiver_handler  # ⬅ هندلر فایل جدید

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # یا مستقیم توکن بذار

app = Application.builder().token(TOKEN).build()

# 🧩 ترتیب مهمه
app.add_handler(registration_conversation)                        # ⬅️ محاوره ثبت‌نام
app.add_handler(CommandHandler("start", start_handler))           # ⬅️ شروع بات
app.add_handler(MessageHandler(filters.Document.ALL, file_receiver_handler))  # ⬅️ دریافت فایل‌ها
app.add_handler(CallbackQueryHandler(handle_callback_query))      # ⬅️ دکمه‌های شیشه‌ای
app.add_handler(MessageHandler(filters.TEXT, handle_menu))        # ⬅️ پیام‌های متنی برای منوها

print("🤖 Bot is running...")
app.run_polling()
