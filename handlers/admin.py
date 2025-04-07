from telegram import Update
from telegram.ext import ContextTypes
from handlers.common import build_keyboard

async def customer_list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👥 لیست مشتریان (در حال توسعه...)")

async def discount_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎁 تنظیم تخفیف مناسبتی (در حال توسعه...)")

async def go_to_admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "main_admin"
    keyboard = build_keyboard("main_admin")
    await update.message.reply_text("🎛 وارد پنل ادمین شدید.", reply_markup=keyboard)
