from telegram.ext import Application, CommandHandler, MessageHandler, filters,CallbackQueryHandler
from menu_manager import handle_menu
from handlers.start import start_handler  # ← هندلر جدید و استاندارد start
from handlers.inline.inline_menu_manager import handle_callback_query
from handlers.register import registration_conversation

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # یا مستقیم توکن بذار

app = Application.builder().token(TOKEN).build()

app.add_handler(registration_conversation)  # ⬅ اول ثبت‌نام
app.add_handler(CommandHandler("start", start_handler))  # ⬅ بعد استارت
app.add_handler(CallbackQueryHandler(handle_callback_query))  # ⬅ بعد شیشه‌ای‌ها
app.add_handler(MessageHandler(filters.TEXT, handle_menu))  # ⬅ آخر بقیه پیام‌ها

print("🤖 Bot is running...")
app.run_polling()
