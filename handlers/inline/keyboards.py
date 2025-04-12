from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from itertools import zip_longest
from .menus import menus, menu_layouts

def chunk_buttons(buttons, size=2):
    return [list(filter(None, group)) for group in zip_longest(*[iter(buttons)] * size)]

def build_inline_keyboard(menu_key: str, context=None, file_db_id: int = None):
    menu = menus.get(menu_key, {})
    layout = menu_layouts.get(menu_key, 2)
    quantity = context.user_data.get("file_quantity", 1) if context else 1

    buttons = []
    for label, callback in menu.items():
        label = label.format(quantity=quantity)

        if callback is None:
            buttons.append(InlineKeyboardButton(text=label, callback_data="noop"))
        else:
            if "{" in callback:
                callback = callback.format(file_id=file_db_id)
            buttons.append(InlineKeyboardButton(text=label, callback_data=callback))

    return InlineKeyboardMarkup(chunk_buttons(buttons, layout))
