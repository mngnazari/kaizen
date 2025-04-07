from telegram import ReplyKeyboardMarkup
from menus import menus
from handlers import dummy_handler

async def handle_menu(update, context, from_where="msg"):
    text = update.message.text if from_where == "msg" else "start"
    current_menu = context.user_data.get("current_menu", "main")
    menu = menus.get(current_menu, {})

    handler = menu.get(text)
    if handler:
        await handler(update, context)
    else:
        keyboard = ReplyKeyboardMarkup([list(menu.keys())], resize_keyboard=True)
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=keyboard)