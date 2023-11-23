from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#-Main_menu-
Dev = KeyboardButton("💻Developer💻")
Slang = KeyboardButton("😎Slang🗣️")
anecdotes_button = KeyboardButton("😄Jokes with slang📖")
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(Slang).add(Dev).add(anecdotes_button)

#-Slang-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Створюємо кнопки для слов в сленгу
slang_buttons = [
    KeyboardButton("😵 Краш 😵"),
    KeyboardButton("✅ Валідний ✅"),
    KeyboardButton("🔄 Дефолт 🔄"),
    KeyboardButton("📘 Юзер Гайд 📘"),
    KeyboardButton("🔗 Клікабельний 🔗"),
    KeyboardButton("📜 Софт скіли 📜"),
    KeyboardButton("📅 Дедлайн 📅"),
    KeyboardButton("🔄 Апдейт 🔄"),
    KeyboardButton("🌐 Айпі 🌐"),
    KeyboardButton("🤝 Митинг 🤝"),
    KeyboardButton("☎ Колл ☎"),
    KeyboardButton("📥 Комміт 📥"),
    KeyboardButton("📄 Парсить 📄"),
    KeyboardButton("🏖️ Пісочниця 🏖️"),
    KeyboardButton("🚀 Релиз 🚀"),
    KeyboardButton("📋 Таска 📋"),
    KeyboardButton("🌟 Фича 🌟"),
    KeyboardButton("🧩 Юнит 🧩"),
    KeyboardButton("🐞 Баг 🐞"),
    KeyboardButton("🤖 Гіт 🤖"),
]

# Розділяємо кнопки по 3 в рядок
rows = [slang_buttons[i:i+2] for i in range(0, len(slang_buttons), 2)]

# Створюємо клавіатуру
slang_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*rows[0])

# Додаємо решту рядків
for row in rows[1:]:
    slang_keyboard.row(*row)

slang_keyboard.add(KeyboardButton("⇐Back to Main Menu"))
