from telegram import Update
from telegram.ext import ContextTypes
import os
from dotenv import load_dotenv

from handlers.common import build_keyboard
from handlers.register import start_registration

# 🧾 بارگذاری متغیرهای محیطی
load_dotenv()
BOT_USERNAME = os.getenv("BOT_USERNAME")
ADMIN_IDS = [int(i.strip()) for i in os.getenv("ADMIN_IDS", "").split(",") if i.strip().isdigit()]

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message
    message_text = message.text

    # 📥 لاگ اولیه
    print(f"📥 /start توسط: {user_id}, متن پیام: {message_text}")

    # 📦 لاگ آرگومان‌های بعد از استارت (مثلاً ref_1234)
    args = context.args if hasattr(context, "args") else []
    print("📦 context.args:", args)

    # ✅ اگر کاربر ادمینه
    if user_id in ADMIN_IDS:
        context.user_data["current_menu"] = "main_admin"
        await message.reply_text(
            "🎛 خوش آمدید مدیر عزیز!",
            reply_markup=build_keyboard("main_admin")
        )
        return

    # ✅ اگر با لینک دعوت اومده
    if args and args[0].startswith("ref_"):
        try:
            inviter_id = int(args[0].replace("ref_", ""))
            context.user_data["inviter_id"] = inviter_id
            print(f"✅ کاربر با لینک دعوت وارد شد. inviter_id = {inviter_id}")
            await start_registration(update, context)
            return
        except ValueError:
            print("❗ کد دعوت نامعتبر بود.")
            pass

    # ⛔ مجاز نیست (نه ادمین، نه با لینک دعوت)
    await message.reply_text("این بات اختصاصی است. برای ثبت‌نام باید لینک دعوت داشته باشید.")
