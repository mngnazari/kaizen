from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import build_inline_keyboard
from .menus import menu_parents
from database.queries import update_quantity, get_file_data_by_unique_id


async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = query.data
    current_menu = context.user_data.get("inline_current_menu")
    file_unique_id = context.user_data.get("inline_file_unique_id")

    print("📥 کلیک دکمه شیشه‌ای:")
    print("• user_id =", user_id)
    print("• data =", data)
    print("• current_menu =", current_menu)
    print("• file_unique_id =", file_unique_id)

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

    if action == "change":
        current = context.user_data.get("file_quantity", 1)
        if payload == "+":
            current += 1
        elif payload == "-" and current > 1:
            current -= 1
        context.user_data["file_quantity"] = current

        print("🔢 مقدار جدید تعداد:", current)

        try:
            await query.edit_message_reply_markup(
                reply_markup=build_inline_keyboard(current_menu, context)
            )
        except Exception as e:
            print("❗ خطا در change:", str(e))
        return

    if action == "confirm_quantity":
        if not file_unique_id:
            print("⚠️ file_unique_id وجود ندارد.")
            return

        quantity = context.user_data.get("file_quantity", 1)
        update_quantity(file_unique_id, quantity)

        file_data = get_file_data_by_unique_id(file_unique_id)
        caption = (
            f"📦 فایل: {file_data['file_name']}\n"
            f"🕒 زمان تحویل: {file_data['delivery_time'] or '—'}\n"
            f"🔢 تعداد: {file_data['quantity']}\n"
            f"📝 توضیحات: {file_data['description'] or '—'}"
        )

        try:
            await query.edit_message_caption(
                caption=caption,
                reply_markup=build_inline_keyboard("file_action_menu", context)
            )
            context.user_data["inline_current_menu"] = "file_action_menu"
        except Exception as e:
            print("❗ خطا در confirm_quantity:", str(e))
        return

    if action == "up":
        parent_menu = menu_parents.get(current_menu)
        if parent_menu:
            context.user_data["inline_current_menu"] = parent_menu
            try:
                await query.edit_message_reply_markup(
                    reply_markup=build_inline_keyboard(parent_menu, context)
                )
            except Exception as e:
                print("❗ خطا در up:", str(e))
        else:
            await query.edit_message_text("🔚 منوی والد یافت نشد.")
        return
