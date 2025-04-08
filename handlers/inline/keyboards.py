from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from .menus import menus, menu_layouts  # ← اضافه کن
from itertools import zip_longest

def chunk_buttons(buttons, size=2):
    return [list(filter(None, group)) for group in zip_longest(*[iter(buttons)] * size)]

def build_inline_keyboard(menu_key, context_data=""):
    menu = menus.get(menu_key, {})
    size = menu_layouts.get(menu_key, 2)  # ← از layout استفاده می‌کنه
    buttons = [
        InlineKeyboardButton(text, callback_data=f"{callback}:{context_data}")
        for text, callback in menu.items()
    ]
    return InlineKeyboardMarkup(chunk_buttons(buttons, size))
