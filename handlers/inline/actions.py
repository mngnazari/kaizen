from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import build_inline_keyboard

async def preview(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    await update.callback_query.edit_message_text(
        text=f"📎 پیش‌نمایش فایل {data}",
        reply_markup=build_inline_keyboard("confirm_menu", data)
    )

async def details(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    await update.callback_query.edit_message_text(
        text=f"📝 توضیحات فایل {data}",
        reply_markup=build_inline_keyboard("confirm_menu", data)
    )

async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    await update.callback_query.edit_message_text(text=f"✅ فایل {data} تأیید شد.")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    await update.callback_query.edit_message_text(text=f"❌ عملیات لغو شد.")

async def back_to(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    await update.callback_query.edit_message_text(
        text=f"🔙 بازگشت",
        reply_markup=build_inline_keyboard(data)
    )
