from telegram import Update
from telegram.ext import ContextTypes
import os
from dotenv import load_dotenv
from handlers.common import build_keyboard


load_dotenv()
BOT_USERNAME = os.getenv("BOT_USERNAME")
raw_ids = os.getenv("ADMIN_IDS", "")
ADMIN_IDS = [int(i.strip()) for i in raw_ids.split(",") if i.strip().isdigit()]

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # اگر کاربر از طریق لینک دعوت اومده
    if context.args and context.args[0].startswith("ref_"):
        referrer_id = context.args[0].split("_")[1]
        await update.message.reply_text(f"🎉 به ربات خوش آمدید! معرف شما: {referrer_id}")
        # اینجا می‌تونی کارهایی مثل ثبت در دیتابیس انجام بدی
        return

    if user_id in ADMIN_IDS:
        context.user_data["current_menu"] = "main_admin"
        keyboard = build_keyboard("main_admin")
        await update.message.reply_text("🎛 خوش آمدید مدیر عزیز!", reply_markup=build_keyboard("main_admin"))
    else:
        await update.message.reply_text("این بات اختصاصی است. برای ثبت‌نام باید لینک دعوت داشته باشید.")