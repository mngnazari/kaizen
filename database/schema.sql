-- 🧑 جدول کاربران
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    username TEXT,
    full_name TEXT,
    phone TEXT,
    is_admin INTEGER DEFAULT 0,
    referred_by INTEGER REFERENCES users(id),
    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP
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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE NOT NULL,
    full_name TEXT,
    is_admin INTEGER DEFAULT 0,             -- 1 = ادمین، 0 = عادی
    referrer_id INTEGER,                    -- آیدی کسی که این کاربر را دعوت کرده
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (referrer_id) REFERENCES users(id)
);
