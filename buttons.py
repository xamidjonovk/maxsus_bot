from telegram import ReplyKeyboardMarkup, KeyboardButton

register_button = ReplyKeyboardMarkup([
    ["📋Ro'yhatdan o'tish"]
], resize_keyboard=True)

directory = ReplyKeyboardMarkup([
    ["💻Data Science", "💻Software Engineering"],
    ["💻Full Stack"]
], resize_keyboard=True)

contact = [
    [KeyboardButton(text="📲Contact Yuborish", request_contact=True)]
]

check = ReplyKeyboardMarkup([
    ["✅Tasdiqlash"]
], resize_keyboard=True)

homework = ReplyKeyboardMarkup([
    ["📚Proyektni topshirish"]
], resize_keyboard=True, one_time_keyboard=True)


admin_buttons = ReplyKeyboardMarkup([
    ["📈Statistika"], ["Statistikani yangilash"]
], resize_keyboard=True)
