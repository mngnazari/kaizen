from telegram import Update
from telegram.ext import ContextTypes
from handlers.common import build_keyboard
import os
from dotenv import load_dotenv

async def customer_list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👥 لیست مشتریان (در حال توسعه...)")

async def discount_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎁 تنظیم تخفیف مناسبتی (در حال توسعه...)")

async def go_to_admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "main_admin"
    keyboard = build_keyboard("main_admin")
    await update.message.reply_text("🎛 وارد پنل ادمین شدید.", reply_markup=keyboard)


async def invite_link_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    load_dotenv()
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    admin_id=os.getenv("ADMIN_IDS")
    invite_link = f"https://t.me/{BOT_USERNAME}?start=ref_{admin_id}"
    await update.message.reply_text(f"🔗 لینک دعوت شما:\n{invite_link}")
