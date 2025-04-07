from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from itertools import zip_longest

# 📐 تنظیم layout منوها
menu_layout = {
    "main_customer": 3,
    "archive_menu": 3,
    "main_admin": 2
}

# ✅ ساخت کیبورد بر اساس layout هر منو
def build_keyboard(menu_key: str):
    from menus import menus  # ← اینجا ایمپورت می‌کنیم تا حلقه ایجاد نشه
    menu = menus.get(menu_key, {})
    buttons = list(menu.keys())
    row_width = menu_layout.get(menu_key, 2)
    rows = [list(filter(None, group)) for group in zip_longest(*[iter(buttons)] * row_width)]
    return ReplyKeyboardMarkup(rows, resize_keyboard=True)

# ⬅️ دکمه بازگشت
async def back_to_main_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "main_customer"
    keyboard = build_keyboard("main_customer")
    await update.message.reply_text("🔙 بازگشت به منوی اصلی", reply_markup=keyboard)
