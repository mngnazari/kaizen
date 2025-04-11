-- 🧑 جدول کاربران
CREATE TABLE users (
    telegram_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT,
    address TEXT,
    inviter_id INTEGER,
    role TEXT DEFAULT 'customer'
);

-- 💳 کیف پول
CREATE TABLE IF NOT EXISTS wallet (
    user_id INTEGER PRIMARY KEY REFERENCES users(id),
    balance INTEGER DEFAULT 0
);

-- 🧾 سفارشات فایل
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    file_name TEXT,
    file_type TEXT,
    file_id TEXT NOT NULL,
    file_unique_id TEXT NOT NULL,   -- ✅ اضافه شده برای شناسایی یکتا
    sent_at TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    description TEXT DEFAULT 'فاقد توضیحات',
    delivery_time TEXT DEFAULT '',
    file_status TEXT DEFAULT 'جدید',
    preview_file_id TEXT DEFAULT '',
    FOREIGN KEY (telegram_id) REFERENCES users (telegram_id)
);


-- 🪙 تراکنش‌های مالی (پرداخت / پاداش / تخفیف)
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    amount INTEGER,
    type TEXT, -- deposit / reward / discount / purchase
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 💬 پیام‌های پشتیبانی
CREATE TABLE IF NOT EXISTS support_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ایجاد جدول کاربران
CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT,
    address TEXT,  -- ← این خط رو اضافه کن
    inviter_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
