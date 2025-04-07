from telegram import Update
from telegram.ext import ContextTypes
from handlers.common import build_keyboard

async def archive_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "archive_menu"
    keyboard = build_keyboard("archive_menu")
    await update.message.reply_text("📂 آرشیو را انتخاب کردید.", reply_markup=keyboard)

async def in_progress_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔄 سفارش‌های در حال انجام شما اینجاست.")

async def wallet_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💳 موجودی کیف پول شما: 0 تومان.")

async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 برای پشتیبانی با ما تماس بگیرید.")

async def rules_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 قوانین استفاده از خدمات...")

async def invoice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧾 فاکتورهای شما هنوز ثبت نشده.")

async def recent_week_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 آرشیو هفته اخیر")

async def recent_month_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📆 آرشیو ماه اخیر")

async def all_archive_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📁 کل سفارشات ثبت‌شده")
