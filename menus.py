## menus.py
from handlers import customer, admin, common

menu_map = {
    "main_customer": {
        "🗂 آرشیو": customer.archive_handler,
        "🔄 در حال انجام": customer.in_progress_handler,
        "💳 کیف پول": customer.wallet_handler,
        "📞 پشتیبانی": customer.support_handler,
        "📜 قوانین": customer.rules_handler,
        "🧾 فاکتور": customer.invoice_handler,
        "🧪 تست دکمه شیشه‌ای": customer.test_inline_menu_handler
    },
    "archive_menu": {
        "📅 هفته اخیر": customer.recent_week_handler,
        "📆 ماه اخیر": customer.recent_month_handler,
        "📁 کل": customer.all_archive_handler,  # تغییر خواهد کرد در مرحله بعد
        "🔙 بازگشت": common.pop_menu,
    },
    "all_archive_menu": {
        "📦 کل1": customer.all_archive_1_handler,
        "📦 کل2": customer.all_archive_2_handler,
        "🔙 بازگشت": common.pop_menu,
    },
    "main_admin": {
        "👥 مشتریان": admin.customer_list_handler,
        "🎁 تخفیف مناسبتی": admin.discount_handler,
        "🔙 بازگشت": common.back_to_main_handler,
    }
}


menu_layout = {
    "main_customer": 2,
    "archive_menu": 1,
    "all_archive_menu": 1,
    "main_admin": 2,
}
