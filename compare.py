from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from database.db import save_user_to_db
# مراحل مکالمه
FULL_NAME, PHONE, ADDRESS = range(3)
# 📌 مرحله اول: شروع ثبت‌نام
async def start_registration(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("👤 لطفاً نام و نام خانوادگی خود را وارد کنید:")
    return FULL_NAME
# 📌 مرحله دوم: دریافت نام
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["full_name"] = update.message.text

    contact_button = KeyboardButton("📱 ارسال شماره تماس", request_contact=True)
    keyboard = [[contact_button]]
    await update.message.reply_text(
        "📞 لطفاً شماره تماس خود را با دکمه زیر ارسال کنید:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
    )
    return PHONE
# 📌 مرحله سوم: دریافت شماره تماس
async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.contact:
        context.user_data["phone"] = update.message.contact.phone_number
    else:
        await update.message.reply_text("❗ لطفاً فقط از دکمه ارسال شماره استفاده کنید.")
        return PHONE

    await update.message.reply_text("🏠 لطفاً آدرس خود را وارد کنید:", reply_markup=ReplyKeyboardRemove())
    return ADDRESS
# 📌 مرحله چهارم: دریافت آدرس و ذخیره اطلاعات
async def get_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["address"] = update.message.text

    telegram_id = update.effective_user.id
    full_name = context.user_data["full_name"]
    phone = context.user_data["phone"]
    address = context.user_data["address"]
    inviter_id = context.user_data.get("inviter_id")

    save_user_to_db(telegram_id, full_name, phone, address, inviter_id)

    await update.message.reply_text("✅ ثبت‌نام با موفقیت انجام شد. خوش آمدید! 🎉")

    from handlers.common import build_keyboard
    keyboard = build_keyboard("main_customer")
    await update.message.reply_text("📋 منوی اصلی:", reply_markup=keyboard)

    return ConversationHandler.END
# 📌 ConversationHandler برای ثبت‌نام (شروع از start_handler انجام می‌شود)
registration_conversation = ConversationHandler(
    entry_points=[],  # شروع توسط استارت هندلر
    states={
        FULL_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        PHONE: [MessageHandler(filters.CONTACT, get_phone)],
        ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_address)],
    },
    fallbacks=[],
)
