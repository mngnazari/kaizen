from telegram import ReplyKeyboardMarkup
from menus import menus
from handlers import dummy_handler
from itertools import zip_longest

def chunk_buttons(buttons, size=3):
    return [list(filter(None, group)) for group in zip_longest(*[iter(buttons)]*size)]

async def handle_menu(update, context, from_where="msg"):
    text = update.message.text if from_where == "msg" else "start"
    current_menu = context.user_data.get("current_menu", "main")
    menu = menus.get(current_menu, {})

    handler = menu.get(text)
    if handler:
        await handler(update, context)
    else:
        #keyboard = ReplyKeyboardMarkup([list(menu.keys())], resize_keyboard=True)
        keyboard = ReplyKeyboardMarkup(chunk_buttons(list(menu.keys()), size=5), resize_keyboard=True)
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=keyboard)