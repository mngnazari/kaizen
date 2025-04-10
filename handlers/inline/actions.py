from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import build_inline_keyboard
from .menus import menu_parents

async def goto(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    keyboard = build_inline_keyboard(payload, "CTX")
    await update.callback_query.edit_message_reply_markup(reply_markup=keyboard)

async def up(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    parent = menu_parents.get(payload)
    if parent:
        keyboard = build_inline_keyboard(parent, "CTX")
        await update.callback_query.edit_message_reply_markup(reply_markup=keyboard)
    else:
        await update.callback_query.edit_message_text("⛔ منوی والد یافت نشد.")

async def preview(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("📄 پیش‌نمایش فایل شما")
    keyboard = build_inline_keyboard(payload, "CTX")

async def details(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("📝 لطفاً توضیحات فایل را ارسال کنید.")

async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("✅ فایل شما تأیید شد.")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("❌ عملیات لغو شد.")

async def option_21(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("🔧 گزینه ۲-۱ انتخاب شد.")

async def option_22(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("📐 گزینه ۲-۲ انتخاب شد.")

async def check_31(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("🔍 بررسی ۳-۱ در حال انجام است.")

async def edit_32(update: Update, context: ContextTypes.DEFAULT_TYPE, payload: str):
    await update.callback_query.edit_message_text("✏️ لطفاً تغییرات خود را وارد کنید.")

    ...
    # 🎯 سایر اکشن‌ها
    if action == "my_orders":
        await query.edit_message_text("📦 لیست سفارشات شما در این بخش نمایش داده می‌شود.")
        return
