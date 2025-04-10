from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from itertools import zip_longest
from .menus import menus, menu_layouts


# ➕ تقسیم دکمه‌ها به ردیف‌هایی با تعداد مشخص
def chunk_buttons(buttons, size=2):
    return [list(filter(None, group)) for group in zip_longest(*[iter(buttons)] * size)]


# 🎛 ساخت کیبورد شیشه‌ای با جایگزینی context در عنوان دکمه‌ها
def build_inline_keyboard(menu_key: str, context=None):
    menu = menus.get(menu_key, {})
    layout = menu_layouts.get(menu_key, 2)

    # دریافت مقادیر context برای جایگزینی در عنوان‌ها
    quantity = 1
    if context:
        quantity = context.user_data.get("file_quantity", 1)

    buttons = []
    for label, callback in menu.items():
        # مقداردهی داینامیک عنوان‌ها
        label = label.format(quantity=quantity)

        if callback is None:
            buttons.append(InlineKeyboardButton(text=label, callback_data="noop"))
        else:
            buttons.append(InlineKeyboardButton(text=label, callback_data=callback))

    return InlineKeyboardMarkup(chunk_buttons(buttons, layout))
