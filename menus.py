from handlers import (
    dummy_handler,
    back_to_main_handler,
    archive_week_handler,
    archive_month_handler,
    archive_all_handler
)

menus = {
    "main": {  # اینو می‌ذاریم به عنوان منوی مشتری
        "📁 آرشیو": dummy_handler,
        "⏳ در حال انجام": dummy_handler,
        "💰 کیف پول": dummy_handler,
        "🆘 پشتیبانی": dummy_handler,
        "📜 قوانین": dummy_handler,
        "🧾 فاکتور": dummy_handler,
    },
    "archive": {
        "📅 هفته اخیر": archive_week_handler,
        "🗓 ماه اخیر": archive_month_handler,
        "📂 کل": archive_all_handler,
        "⬅️ بازگشت": back_to_main_handler
    }
}
