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


# 📌 ثبت منوی جدید در history و current_menu
def push_menu(context: ContextTypes.DEFAULT_TYPE, menu_key: str, max_depth: int = 10):
    context.user_data["current_menu"] = menu_key
    history = context.user_data.setdefault("menu_history", [])
    print("🧭 push_menu به:", menu_key)  # 👈 لاگ دیباگ

    if not history or history[-1] != menu_key:
        history.append(menu_key)

    if len(history) > max_depth:
        history.pop(0)


# 🔙 برگشت به منوی قبلی
async def pop_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    history = context.user_data.get("menu_history", [])

    if len(history) > 1:
        history.pop()
        prev_menu = history[-1]
        context.user_data["current_menu"] = prev_menu

        from handlers.common import build_keyboard  # ⬅️ همینجا می‌سازیم کیبورد
        keyboard = build_keyboard(prev_menu)
        await update.message.reply_text("↩️ بازگشت به منوی قبل:", reply_markup=keyboard)

    else:
        await update.message.reply_text("در منوی اصلی هستید.")

# 🏠 بازگشت مستقیم به منوی اصلی
async def back_to_main_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "main_customer"
    context.user_data["menu_history"] = ["main_customer"]

    from menu_manager import handle_menu
    await handle_menu(update, context)
