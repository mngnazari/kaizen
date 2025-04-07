# نیازی نیست handle_menu رو بالا import کنیم

# تابع تست ساده
async def dummy_handler(update, context):
    await update.message.reply_text("✅ تابع مربوط به دکمه اجرا شد.")

# تنظیمات: وارد کردن handle_menu فقط وقتی لازمه
async def settings_handler(update, context):
    from menu_manager import handle_menu  # ایمپورت داخل تابع
    context.user_data['current_menu'] = 'settings'
    await handle_menu(update, context)

# بازگشت: وارد کردن handle_menu فقط وقتی لازمه
async def back_to_main_handler(update, context):
    from menu_manager import handle_menu  # ایمپورت داخل تابع
    context.user_data['current_menu'] = 'main'
    await handle_menu(update, context)
