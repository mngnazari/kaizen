from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from .menus import menus

def build_inline_keyboard(menu_key, context_data=""):
    menu = menus.get(menu_key, {})
    keyboard = []
    for label, action in menu.items():
        callback = f"{action}:{context_data}" if context_data else action
        keyboard.append([InlineKeyboardButton(label, callback_data=callback)])
    return InlineKeyboardMarkup(keyboard)
