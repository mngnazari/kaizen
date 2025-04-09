from handlers import customer, admin, common

# 🧭 نگاشت منوها به توابع مربوطه
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
        "📁 کل": customer.all_archive_handler,
        "🔙 بازگشت": "UP"
    },
    "all_archive_menu": {
        "📄 کل 1": customer.all1_handler,
        "📂 کل 2": customer.all2_handler,
        "🔙 بازگشت": "UP",  # اشاره به منوی والد
    },
    "main_admin": {
        "👥 مشتریان": admin.customer_list_handler,
        "🎁 تخفیف مناسبتی": admin.discount_handler,
        "🔙 بازگشت": "UP"
    }
}

# 🎛 کنترل تعداد دکمه در هر ردیف از هر منو
menu_layout = {
    "main_customer": 2,
    "archive_menu": 1,
    "main_admin": 2
}

# ⬆️ مشخص کردن منوی والد برای هر منو (برای دکمه بازگشت Up)
menu_parents = {
    "archive_menu": "main_customer",
    "all_archive_menu": "archive_menu",
}
