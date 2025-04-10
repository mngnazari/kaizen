from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
import os

from handlers.common import build_keyboard
#from database.db import add_user  # اگر بعداً اتصال به دیتابیس نیاز شد

# 🧩 مراحل گفت‌وگو
FULL_NAME, PHONE, ADDRESS = range(3)


async def start_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    referral = context.args[0] if context.args and context.args[0].startswith("ref_") else None
    if referral:
        context.user_data["referral"] = referral.replace("ref_", "")
        await update.message.reply_text("👤 لطفاً نام و نام خانوادگی خود را وارد کنید:")
        return FULL_NAME
    else:
        await update.message.reply_text("❌ لینک ثبت‌نام معتبر نیست.")
        return ConversationHandler.END


async def get_full_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["full_name"] = update.message.text
    contact_button = KeyboardButton("📱 ارسال شماره تماس", request_contact=True)
    markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("☎️ لطفاً شماره تماس خود را ارسال کنید:", reply_markup=markup)
    return PHONE


async def get_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.contact:
        context.user_data["phone"] = update.message.contact.phone_number
        await update.message.reply_text("📍 لطفاً آدرس خود را وارد کنید:", reply_markup=ReplyKeyboardRemove())
        return ADDRESS
    else:
        await update.message.reply_text("لطفاً از دکمه ارسال شماره استفاده کنید.")
        return PHONE


async def get_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["address"] = update.message.text

    # اینجا می‌تونی اطلاعات رو توی دیتابیس ذخیره کنی
    # مثلا:
    # add_user(
    #     user_id=update.effective_user.id,
    #     full_name=context.user_data["full_name"],
    #     phone=context.user_data["phone"],
    #     address=context.user_data["address"],
    #     referrer_id=context.user_data.get("referral")
    # )

    # ست کردن منوی مشتری
    context.user_data["current_menu"] = "main_customer"
    await update.message.reply_text("✅ ثبت‌نام با موفقیت انجام شد.", reply_markup=build_keyboard("main_customer"))
    return ConversationHandler.END


registration_conversation = ConversationHandler(
    entry_points=[CommandHandler("start", start_register)],
    states={
        FULL_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_full_name)],
        PHONE: [MessageHandler(filters.CONTACT, get_contact)],
        ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_address)],
    },
    fallbacks=[],
)
