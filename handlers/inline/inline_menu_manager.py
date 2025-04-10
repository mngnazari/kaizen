from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import build_inline_keyboard
from .menus import menu_parents


async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    current_menu = context.user_data.get("inline_current_menu")
    print("📂 current_menu:", current_menu)

    data = query.data
    if ":" in data:
        action, payload = data.split(":", 1)
    else:
        action, payload = data, ""

    if action == "goto":
        context.user_data["inline_current_menu"] = payload
        await query.edit_message_reply_markup(
            reply_markup=build_inline_keyboard(payload, context)
        )
        return

    elif action == "up":
        parent_menu = menu_parents.get(current_menu)
        if parent_menu:
            context.user_data["inline_current_menu"] = parent_menu
            await query.edit_message_reply_markup(
                reply_markup=build_inline_keyboard(parent_menu, context)
            )
        else:
            await query.edit_message_text("🔚 منوی والد یافت نشد.")
        return

    elif action == "change":
        current = context.user_data.get("file_quantity", 1)
        if payload == "+":
            current += 1
        elif payload == "-" and current > 1:
            current -= 1
        context.user_data["file_quantity"] = current

        await query.edit_message_reply_markup(
            reply_markup=build_inline_keyboard(current_menu, context)
        )
        return

    else:
        await query.edit_message_text(f"✅ شما «{action}» را انتخاب کردید.")
