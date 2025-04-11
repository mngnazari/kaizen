# فایل: handlers/start.py

from telegram import Update
from telegram.ext import ContextTypes
import os
from dotenv import load_dotenv

from handlers.common import build_keyboard
from handlers.register import start_registration

load_dotenv()
BOT_USERNAME = os.getenv("BOT_USERNAME")
ADMIN_IDS = [int(i.strip()) for i in os.getenv("ADMIN_IDS", "").split(",") if i.strip().isdigit()]

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message

    # 🔄 پاکسازی دیتاهای گفت‌وگوی قبلی
    context.user_data.clear()

    # ✅ اگر ادمینه
    if user_id in ADMIN_IDS:
        context.user_data["current_menu"] = "main_admin"
        await message.reply_text(
            "🎛 خوش آمدید مدیر عزیز!",
            reply_markup=build_keyboard("main_admin")
        )
        return

    # ✅ اگر با لینک دعوت وارد شده
    args = context.args
    if args and args[0].startswith("ref_"):
        try:
            referrer_id = int(args[0].replace("ref_", ""))
            context.user_data["inviter_id"] = referrer_id
            await start_registration(update, context)
            return
        except ValueError:
            pass  # کد ref نامعتبر بود

    # ⛔ در غیر این صورت اجازه ثبت‌نام نیست
    await message.reply_text("این بات اختصاصی است. برای ثبت‌نام باید لینک دعوت داشته باشید.")
