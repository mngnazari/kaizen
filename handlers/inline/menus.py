menus = {
    "file_action_menu": {
        "🔢 تغییر تعداد": "goto:quantity_menu",
        "⏩ زودتر": "rush",
        "📝 توضیحات": "description",
        "❌ انصراف": "cancel_file"
    },
    "quantity_menu": {
        "➖": "change:-",
        "🔢 تعداد: {quantity}": None,  # ← مقدار داینامیک
        "➕": "change:+",
        "✅ تأیید": "up",
        "❌ انصراف": "up"
    }
}

menu_layouts = {
    "file_action_menu": 3,
    "quantity_menu": 3
}

menu_parents = {
    "quantity_menu": "file_action_menu"
}
