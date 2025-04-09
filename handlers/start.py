from telegram import Update
from telegram.ext import ContextTypes
from handlers.common import build_keyboard
from handlers.common import build_keyboard

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "main_customer"
    keyboard = build_keyboard("main_customer")
    await update.message.reply_text("سلام! به ربات خدمات پرینت سه‌بعدی خوش آمدید 😊", reply_markup=keyboard)
