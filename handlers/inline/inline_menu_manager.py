from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from handlers.inline.keyboards import build_inline_keyboard
from handlers.inline.menus import menu_parents
from database.queries import (
    update_quantity_by_id,
    get_file_data_by_id,
    update_description_by_id
)

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if ":" in data:
        action, payload = data.split(":", 1)
    else:
        action, payload = data, ""

    current_menu = context.user_data.get("inline_current_menu")
    file_db_id = int(payload) if payload.isdigit() else context.user_data.get("file_db_id")

    print("📥 کلیک دکمه شیشه‌ای:")
    print("• action =", action)
    print("• payload =", payload)
    print("• file_db_id =", file_db_id)
    print("• current_menu =", current_menu)

    if action == "goto":
        context.user_data["inline_current_menu"] = payload
        await query.edit_message_reply_markup(
            reply_markup=build_inline_keyboard(payload, context, file_db_id)
        )
        return

    elif action == "up":
        parent = menu_parents.get(current_menu)
        if parent:
            context.user_data["inline_current_menu"] = parent
            await query.edit_message_reply_markup(
                reply_markup=build_inline_keyboard(parent, context, file_db_id)
            )
        return

    elif action == "change":
        key = f"quantity_{file_db_id}"
        quantity = context.user_data.get(key, 1)
        if payload == "+":
            quantity += 1
        elif payload == "-" and quantity > 1:
            quantity -= 1
        context.user_data[key] = quantity

        try:
            await query.edit_message_reply_markup(
                reply_markup=build_inline_keyboard(current_menu, context, file_db_id)
            )
        except Exception as e:
            if "Message is not modified" in str(e):
                print("⚠️ تغییری در دکمه‌ها ایجاد نشده. کیبورد قبلی مشابه بوده.")
            else:
                print("❗ خطا در تغییر دکمه‌ها:", e)
        return

    elif action == "confirm_quantity":
        quantity = context.user_data.get(f"quantity_{file_db_id}", 1)
        update_quantity_by_id(file_db_id, quantity)
        file_data = get_file_data_by_id(file_db_id)
        if not file_data:
            await query.message.reply_text("❗ خطا در دریافت اطلاعات فایل.")
            return

        caption = (
            f"📦 فایل: {file_data['file_name']}\n"
            f"🕒 زمان تحویل: {file_data['delivery_time'] or '—'}\n"
            f"🔢 تعداد: {file_data['quantity']}\n"
            f"📝 توضیحات: {file_data['description'] or '—'}"
        )

        msg_info = context.user_data.get(f"file_msg_{file_db_id}")
        if msg_info:
            await context.bot.edit_message_caption(
                chat_id=msg_info["chat_id"],
                message_id=msg_info["message_id"],
                caption=caption,
                parse_mode=ParseMode.HTML,
                reply_markup=build_inline_keyboard("file_action_menu", context, file_db_id)
            )
        return

    elif action == "description":
        context.user_data["awaiting_description_file_id"] = file_db_id
        await query.message.reply_text("📝 لطفاً توضیحات مورد نظر خود را وارد کنید:")
        return

    elif action == "rush":
        await query.message.reply_text("⏩ فایل شما در اولویت بررسی قرار گرفت.")
        return

    elif action == "preview":
        await query.message.reply_text("📄 پیش‌نمایش فایل در حال آماده‌سازی است.")
        return

    elif action == "cancel_file":
        await query.message.reply_text("❌ عملیات مربوط به این فایل لغو شد.")
        return

    elif action == "noop":
        await query.answer("⏳ بدون عملکرد خاص")
        return

    elif action == "option_21":
        await query.message.reply_text("🔧 گزینه ۲-۱ انتخاب شد.")
        return

    elif action == "option_22":
        await query.message.reply_text("📐 گزینه ۲-۲ انتخاب شد.")
        return

    elif action == "check_31":
        await query.message.reply_text("🔍 بررسی ۳-۱ در حال انجام است.")
        return

    elif action == "edit_32":
        await query.message.reply_text("✏️ لطفاً تغییرات خود را وارد کنید.")
        return

    else:
        await query.message.reply_text("❗ عملیات نامعتبر یا ناشناخته.")
        return
