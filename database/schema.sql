-- 🧑 جدول کاربران
CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT,
    address TEXT,
    inviter_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 💳 کیف پول
CREATE TABLE IF NOT EXISTS wallet (
    user_id INTEGER PRIMARY KEY REFERENCES users(id),
    balance INTEGER DEFAULT 0
);

-- 🧾 سفارشات فایل
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    file_id TEXT,
    caption TEXT,
    quantity INTEGER DEFAULT 1,
    is_rush INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'pending'
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
