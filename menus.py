## menus.py
from handlers import customer, admin, common

menus = {
    "main_customer": {
        "🗂 آرشیو": customer.archive_handler,
        "🔄 در حال انجام": customer.in_progress_handler,
        "💳 کیف پول": customer.wallet_handler,
        "📞 پشتیبانی": customer.support_handler,
        "📜 قوانین": customer.rules_handler,
        "🧾 فاکتور": customer.invoice_handler,
    },
    "archive_menu": {
        "📅 هفته اخیر": customer.recent_week_handler,
        "📆 ماه اخیر": customer.recent_month_handler,
        "📁 کل": customer.all_archive_handler,
        "🔙 بازگشت": common.back_to_main_handler,
    },
    "main_admin": {
        "👥 مشتریان": admin.customer_list_handler,
        "🎁 تخفیف مناسبتی": admin.discount_handler,
        "🔙 بازگشت": common.back_to_main_handler,
    }
} 