from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from itertools import zip_longest




# ➕ تقسیم دکمه‌ها به ردیف‌هایی با تعداد مشخص
def chunk_buttons(buttons, size=2):
    return [list(filter(None, group)) for group in zip_longest(*[iter(buttons)] * size)]


# 🎛 ساخت کیبورد بر اساس منوی فعلی و layout دکمه‌ها
def build_keyboard(menu_key: str):
    from menus import menu_map, menu_layout
    menu = menu_map.get(menu_key, {})
    layout_size = menu_layout.get(menu_key, 2)  # پیش‌فرض ۲ دکمه در هر ردیف
    buttons = list(menu.keys())
    keyboard = chunk_buttons(buttons, layout_size)
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ⬆️ بازگشت به منوی والد (Up)
async def up_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from menus import menu_parents
    current_menu = context.user_data.get("current_menu")
    parent_menu = menu_parents.get(current_menu)

    if parent_menu:
        context.user_data["current_menu"] = parent_menu
        keyboard = build_keyboard(parent_menu)
        await update.message.reply_text("↩ بازگشت به منوی قبلی", reply_markup=keyboard)
    else:
        await update.message.reply_text("🔸 در منوی اصلی هستید.")

# 🏠 بازگشت مستقیم به منوی اصلی
async def back_to_main_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "main_customer"
    context.user_data["menu_history"] = ["main_customer"]

    from menu_manager import handle_menu
    await handle_menu(update, context)
