async def dummy_handler(update, context):
    await update.message.reply_text("✅ این بخش در دست ساخت است.")

async def archive_week_handler(update, context):
    await update.message.reply_text("📅 نمایش آرشیو هفته اخیر...")

async def archive_month_handler(update, context):
    await update.message.reply_text("🗓 نمایش آرشیو ماه اخیر...")

async def archive_all_handler(update, context):
    await update.message.reply_text("📂 نمایش کل آرشیو...")

async def back_to_main_handler(update, context):
    from menu_manager import handle_menu  # lazy import برای جلوگیری از حلقه
    context.user_data['current_menu'] = 'main'
    await handle_menu(update, context)
