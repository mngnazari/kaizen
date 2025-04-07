from telegram.ext import Application, CommandHandler, MessageHandler, filters
from menu_manager import handle_menu
from handlers.start import start_handler  # ← هندلر جدید و استاندارد start

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # یا مستقیم توکن بذار

app = Application.builder().token(TOKEN).build()

# ⬅️ اول CommandHandlerها (مثل /start) باید بیان
app.add_handler(CommandHandler("start", start_handler))

# ⬅️ بعدش MessageHandler عمومی
app.add_handler(MessageHandler(filters.TEXT, handle_menu))

print("🤖 Bot is running...")
app.run_polling()
