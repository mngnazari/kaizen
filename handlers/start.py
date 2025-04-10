from telegram import Update
from telegram.ext import ContextTypes
import os
from dotenv import load_dotenv

from handlers.common import build_keyboard
from handlers.register import start_registration  # ✅ تابع آغاز ثبت‌نام

# بارگذاری .env و لیست ادمین‌ها
load_dotenv()
BOT_USERNAME = os.getenv("BOT_USERNAME")
raw_ids = os.getenv("ADMIN_IDS", "")
ADMIN_IDS = [int(i.strip()) for i in raw_ids.split(",") if i.strip().isdigit()]

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message

    # بررسی اینکه آیا کاربر ادمینه یا نه
    if user_id in ADMIN_IDS:
        context.user_data["current_menu"] = "main_admin"
        keyboard = build_keyboard("main_admin")
        await message.reply_text("🎛 خوش آمدید مدیر عزیز!", reply_markup=keyboard)
        return

    # اگر کاربر از طریق لینک دعوت اومده باشه → شروع ثبت‌نام
    args = context.args
    if args and args[0].startswith("ref_"):
        referrer_id = args[0].replace("ref_", "")
        context.user_data["referrer_id"] = referrer_id
        await start_register(update, context)
        return

    # اگر نه ادمینه و نه از لینک دعوت اومده → اجازه ورود نداره
    await message.reply_text("این بات اختصاصی است. برای ثبت‌نام باید لینک دعوت داشته باشید.")
