from handlers import dummy_handler, settings_handler, back_to_main_handler

menus = {
    "main": {
        "🧪 تست": dummy_handler,
        "⚙️ تنظیمات": settings_handler,
        "📊 درباره ما": dummy_handler
    },
    "settings": {
        "🖼 تغییر پروفایل": dummy_handler,
        "🔕 قطع اعلان": dummy_handler,
        "⬅️ بازگشت": back_to_main_handler
    }
}
