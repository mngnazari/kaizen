from telegram import Update
from telegram.ext import ContextTypes
from handlers.common import build_keyboard
from handlers.inline.keyboards import build_inline_keyboard


# 🗂 آرشیو - منوی جدید → پس push_menu
async def archive_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["current_menu"] = "archive_menu"  # 👈 حتماً لازم
    keyboard = build_keyboard("archive_menu")
    await update.message.reply_text("📂 آرشیو را انتخاب کردید.", reply_markup=keyboard)

# 🔄 در حال انجام - فقط پیام → بدون push_menu
async def in_progress_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔄 سفارش‌های در حال انجام شما اینجاست.")

# 💳 کیف پول - فقط پیام → بدون push_menu
async def wallet_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💳 موجودی کیف پول شما: 0 تومان.")

# 📞 پشتیبانی - فقط پیام → بدون push_menu
async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 برای پشتیبانی با ما تماس بگیرید.")

# 📜 قوانین - فقط پیام → بدون push_menu
async def rules_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 قوانین استفاده از خدمات...")

# 🧾 فاکتور - فقط پیام → بدون push_menu
async def invoice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧾 فاکتورهای شما هنوز ثبت نشده.")

# 📅 هفته اخیر - فقط پیام → بدون push_menu
async def recent_week_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 آرشیو هفته اخیر")
# 📆 ماه اخیر - فقط پیام → بدون push_menu
async def recent_month_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📆 آرشیو ماه اخیر")

# 📁 کل - فقط پیام → بدون push_menu
async def all_archive_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📁 کل سفارشات ثبت‌شده")

# 🧪 تست منوی شیشه‌ای - منوی جدید inline → push_menu اختیاری نیست
async def test_inline_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔘 تست منوی شیشه‌ای:",
       # reply_markup=build_inline_keyboard("file_action_menu", "TEST001")
        reply_markup = build_inline_keyboard("file_action_menu", context)
    )
    context.user_data["inline_current_menu"] = "file_action_menu"

async def all_archive_handler(update, context):
    context.user_data["current_menu"] = "all_archive_menu"
    keyboard = build_keyboard("all_archive_menu")
    await update.message.reply_text("📁 انتخاب بخش از کل آرشیو:", reply_markup=keyboard)

async def all_archive_1_handler(update, context):
    await update.message.reply_text("📦 نمایش کل1")

async def all_archive_2_handler(update, context):
    await update.message.reply_text("📦 نمایش کل2")

async def all1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📄 اطلاعات کل 1")

async def all2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📂 اطلاعات کل 2")
