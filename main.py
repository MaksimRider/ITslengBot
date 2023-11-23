import aiogram
from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
from Keyboard import main_menu, slang_keyboard
import random

TOKEN = "6819270462:AAG0CtpEwNQdwpjEs1dR-A8uTe-3tZH9ges"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

anecdotes = [
    "Why do programmers always advise not to do fixes on Fridays? Because it can cause a 'signed-off task' on the weekends!",
    "If you write robust code but don't document it, it's like making it clickable but not letting users take it.",
    "A programmer's deadline is that moment when you wake up in the morning and already know what you should have done yesterday.",
    "Why do programmers love the color black? It's the default!",
    "If your User Guide becomes popular, it's not yet a feature. But if it helps fix bugs, then it's already a feature!",
    "How do programmers maintain their IP addresses? By changing them frequently, like phone numbers.",
    "Why doesn't a programmer like talking on the phone? Because every Call can become an unapproved Commit.",
    "When programmers say 'Release,' they don't always mean a new product. Sometimes it's just an afternoon release in the fresh air.",
    "If you send a bug report but don't get a response, it might be 'lost in parsing.'",
    "Git is like a meeting: often, you don't understand what they're saying, but you still have to participate."
    "4 years of learning to be a programmer hop hop and you are a barista"
]

def get_random_anecdote():
    return random.choice(anecdotes)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.first_name
    await message.reply(f"🇺🇦Привіт, {user_name}! Я ІТ сленг бот. Допоможу розібратись з ІТ сленгом.\n🇬🇧Hi {user_name}! I'm an IT slang bot. Let me help you understand IT slang.")
    await message.answer("🇺🇦Ось головне меню:\n🇬🇧Here is the main menu:", reply_markup=main_menu)

@dp.message_handler()
async def main(message: types.Message):
    if message.text == "😎Slang🗣️":
        await message.answer("🇺🇦Виберіть слово\n🇬🇧Choose a word",reply_markup=slang_keyboard)

    elif message.text == "😵 Краш 😵":
        await message.answer(
            "🇺🇦 UKR: 😵 Краш 😵\n🇬🇧 ENG: 😵 Crash 😵\n🎤📄 Transcription: /kræʃ/\n📝 Description: Sudden failure of a program.\n🇺🇦 USING ENG: This program has crashed.\n🇺🇦 USING UKR: Ця програма крашнулась.")

    elif message.text == "✅ Валідний ✅":
        await message.answer(
            "🇺🇦 UKR: ✅ Валідний ✅\n🇬🇧 ENG: ✅ Valid ✅\n🎤📄 Transcription: /ˈvælɪd/\n📝 Description: Meeting the necessary criteria or standards.\n🇺🇦 USING ENG: The input is valid.\n🇺🇦 USING UKR: Введені дані є валідними.")

    elif message.text == "🔄 Дефолт 🔄":
        await message.answer(
            "🇺🇦 UKR: 🔄 Дефолт 🔄\n🇬🇧 ENG: 🔄 Default 🔄\n🎤📄 Transcription: /dɪˈfɔlt/\n📝 Description: A standard or pre-set value or option.\n🇺🇦 USING ENG: Unless specified otherwise, it will use the default value.\n🇺🇦 USING UKR: Якщо не вказано інше, буде використовуватися значення за замовчуванням.")

    elif message.text == "📘 Юзер Гайд 📘":
        await message.answer(
            "🇺🇦 UKR: 📘 Юзер Гайд 📘\n🇬🇧 ENG: 📘 User Guide 📘\n🎤📄 Transcription: /ˈjuːzər ɡaɪd/\n📝 Description: A document providing instructions for using a system or product.\n🇺🇦 USING ENG: Refer to the User Guide for instructions.\n🇺🇦 USING UKR: Дивіться посібник користувача для інструкцій.")

    elif message.text == "🔗 Клікабельний 🔗":
        await message.answer(
            "🇺🇦 UKR: 🔗 Клікабельний 🔗\n🇬🇧 ENG: 🔗 Clickable 🔗\n🎤📄 Transcription: /ˈklɪkəbl̩/\n📝 Description: Capable of being clicked with a mouse or similar device.\n🇺🇦 USING ENG: This button is clickable.\n🇺🇦 USING UKR: Цю кнопку можна клікнути.")

    elif message.text == "📜 Софт скіли 📜":
        await message.answer(
            "🇺🇦 UKR: 💼 Софт скіли 💼\n🇬🇧 ENG: 💼 Soft skills 💼\n🎤📄 Transcription: /sɔft skɪlz/\n📝 Description: Personal attributes that enable someone to interact effectively with others.\n🇺🇦 USING ENG: Develop your soft skills for better communication with colleagues.\n🇺🇦 USING UKR: Розвивайте свої м'які навички для кращого спілкування з колегами.")

    elif message.text == "📅 Дедлайн 📅":
        await message.answer(
            "🇺🇦 UKR: 📅 Дедлайн 📅\n🇬🇧 ENG: 📅 Deadline 📅\n🎤📄 Transcription: /ˈdɛdˌlaɪn/\n📝 Description: The time by which something must be completed.\n🇺🇦 USING ENG: We have a strict deadline - finish the work by the end of the week.\n🇺🇦 USING UKR: У нас строгий термін - завершіть роботу до кінця тижня.")

    elif message.text == "🔄 Апдейт 🔄":
        await message.answer(
            "🇺🇦 UKR: 🔄 Апдейт 🔄\n🇬🇧 ENG: 🔄 Update 🔄\n🎤📄 Transcription: /ʌpˈdeɪt/\n📝 Description: The latest version or improvement of a software or system.\n🇺🇦 USING ENG: Don't forget to install the latest update for improved security.\n🇺🇦 USING UKR: Не забудьте встановити останнє оновлення для покращення безпеки.")

    elif message.text == "🌐 Айпі 🌐":
        await message.answer(
            "🇺🇦 UKR: 🌐 Айпі 🌐\n🇬🇧 ENG: 🌐 IP 🌐\n🎤📄 Transcription: /aɪ piː/\n📝 Description: Internet Protocol address, a numerical label assigned to each device participating in a computer network.\n🇺🇦 USING ENG: Check your device's IP address in the network settings.\n🇺🇦 USING UKR: Перевірте IP-адресу свого пристрою в налаштуваннях мережі.")

    elif message.text == "🤝 Митинг 🤝":
        await message.answer(
            "🇺🇦 UKR: 🤝 Митинг 🤝\n🇬🇧 ENG: 🤝 Meeting 🤝\n🎤📄 Transcription: /ˈmitɪŋ/\n📝 Description: An organized gathering of people for a particular purpose.\n🇺🇦 USING ENG: We have an important meeting at 3 PM.\n🇺🇦 USING UKR: Маємо важливу зустріч о 3 годині.")

    elif message.text == "☎ Колл ☎":
        await message.answer(
            "🇺🇦 UKR: ☎️ Колл ☎️\n🇬🇧 ENG: ☎️ Call ☎️\n🎤📄 Transcription: /kɔːl/\n📝 Description: To communicate with someone by telephone.\n🇺🇦 USING ENG: I'll give you a call after the meeting.\n🇺🇦 USING UKR: Я подзвоню вам після зустрічі.")

    elif message.text == "📥 Комміт 📥":
        await message.answer(
            "🇺🇦 UKR: 📥 Комміт 📥\n🇬🇧 ENG: 📥 Commit 📥\n🎤📄 Transcription: /kəˈmɪt/\n📝 Description: To save changes to a repository.\n🇺🇦 USING ENG: Don't forget to commit your changes.\n🇺🇦 USING UKR: Не забудьте закомітити зміни.")

    elif message.text == "📄 Парсить 📄":
        await message.answer(
            "🇺🇦 UKR: 📄 Парсить 📄\n🇬🇧 ENG: 📄 Parse 📄\n🎤📄 Transcription: /pɑːrs/\n📝 Description: To analyze a string of symbols.\n🇺🇦 USING ENG: The program needs to parse the data.\n🇺🇦 USING UKR: Програмі потрібно парсити дані.")

    elif message.text == "🏖️ Пісочниця 🏖️":
        await message.answer(
            "🇺🇦 UKR: 🏖️ Пісочниця 🏖️\n🇬🇧 ENG: 🏖️ Sandbox 🏖️\n🎤📄 Transcription: /ˈsændˌbɒks/\n📝 Description: A testing environment that isolates untested code changes.\n🇺🇦 USING ENG: Test your code in a sandbox before deploying it.\n🇺🇦 USING UKR: Тестуйте свій код у пісочниці перед розгортанням.")

    elif message.text == "🚀 Релиз 🚀":
        await message.answer(
            "🇺🇦 UKR: 🚀 Релиз 🚀\n🇬🇧 ENG: 🚀 Release 🚀\n🎤📄 Transcription: /rɪˈliːs/\n📝 Description: The distribution of a new version of a software product.\n🇺🇦 USING ENG: The release of the new software is scheduled for next week.\n🇺🇦 USING UKR: Реліз нового програмного забезпечення запланований на наступний тиждень.")

    elif message.text == "📋 Таска 📋":
        await message.answer(
            "🇺🇦 UKR: 📋 Таска 📋\n🇬🇧 ENG: 📋 Task 📋\n🎤📄 Transcription: /tæsk/\n📝 Description: A piece of work to be done or undertaken.\n🇺🇦 USING ENG: I have a few tasks to complete before the end of the day.\n🇺🇦 USING UKR: У мене є кілька завдань, які потрібно завершити до кінця дня.")

    elif message.text == "🌟 Фича 🌟":
        await message.answer(
            "🇺🇦 UKR: 🌟 Фича 🌟\n🇬🇧 ENG: 🌟 Feature 🌟\n🎤📄 Transcription: /ˈfiːtʃər/\n📝 Description: A distinctive attribute or aspect of something.\n🇺🇦 USING ENG: The new feature enhances the user experience.\n🇺🇦 USING UKR: Нова фіча покращує користувацький досвід.")

    elif message.text == "🧩 Юнит 🧩":
        await message.answer(
            "🇺🇦 UKR: 🧩 Юнит 🧩\n🇬🇧 ENG: 🧩 Unit 🧩\n🎤📄 Transcription: /ˈjuːnɪt/\n📝 Description: An individual part or element of a system or whole.\n🇺🇦 USING ENG: Test each unit of code separately.\n🇺🇦 USING UKR: Тестуйте кожний юніт коду окремо.")


    elif message.text == "🐞 Баг 🐞":
        await message.answer(
            "🇺🇦 UKR: 🐞 Баг 🐞\n🇬🇧 ENG: 🐞 Bug 🐞\n🎤📄 Transcription: /bʌɡ/\n📝 Description: An error or flaw in a software program.\n🇬🇧 USING ENG: The developers are working to fix the bug. 😊\n🇺🇦 USING UKR: Розробники працюють над виправленням багу. 😊")

    elif message.text == "🤖 Гіт 🤖":
        await message.answer(
            "🇺🇦 UKR: 🤖 Гіт 🤖\n🇬🇧 ENG: 🤖 Git 🤖\n🎤📄 Transcription: /ɡɪt/\n📝 Description: A distributed version control system.\n🇬🇧 USING ENG: Store your code in a repository using Git. 😊\n🇺🇦 USING UKR: Зберігайте свій код у репозиторії за допомогою Git. 😊")

    elif message.text == "⇐Back to Main Menu":
        await message.answer("🇺🇦Ось головне меню:\n🇬🇧Here is the main menu:", reply_markup=main_menu)

    elif message.text == "💻Developer💻":
        await message.answer("👑 OWNERS 👑\n\n👤 The owner of this bot is only @MaksimDeyneka 👤\n\n🌞 Good day! 🌞")

    elif message.text == "😄Jokes with slang📖":
            anecdote = get_random_anecdote()
            await message.answer(anecdote)

    else:
        await message.answer("Виберіть слово або кнопку на клавіатурі")




if __name__ == '__main__':
    executor.start_polling(dp)
    # asyncio.get_event_loop().run_forever()


