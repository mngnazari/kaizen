# فایل: main.py

from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from menu_manager import handle_menu
from handlers.register import registration_conversation
from handlers.start import start_handler
from handlers.inline.inline_menu_manager import handle_callback_query
from handlers.file_handler import file_receiver_handler

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

# ترتیب دقیق هندلرها
app.add_handler(registration_conversation)                                   # ⬅️ محاوره ثبت‌نام
app.add_handler(MessageHandler(filters.Document.ALL, file_receiver_handler)) # ⬅️ دریافت فایل
app.add_handler(CallbackQueryHandler(handle_callback_query))                 # ⬅️ دکمه‌های شیشه‌ای
app.add_handler(CommandHandler("start", start_handler))                      # ⬅️ استارت برای ادمین و غیرمجاز
app.add_handler(MessageHandler(filters.TEXT, handle_menu))                   # ⬅️ پیام‌های متنی معمولی

print("🤖 Bot is running...")
app.run_polling()
