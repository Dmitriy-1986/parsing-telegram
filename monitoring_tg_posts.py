from telethon.sync import TelegramClient
from datetime import datetime, timedelta, timezone

# 🔑 Вставьте API ID и API Hash
API_ID = 21002229  # API ID
API_HASH = 'ef86b3d8721805538b11a9ce26626c91'  # API Hash
KEYWORD = "ЗАЭС"  # Ключевое слово для поиска

# 📅 Даты поиска (переводим в UTC)
DATE_FROM = datetime(2025, 1, 1, tzinfo=timezone.utc)  # Начало поиска
DATE_TO = datetime(2025, 2, 19, tzinfo=timezone.utc)    # Конец поиска

# 🔍 Список каналов и их ID
CHANNELS = {
    "РИА Новости": -1001101170442,
    "НОВОСТИ ЭНЕРГОДАРА 🇷🇺": -1002052735283,
    "Операция Z: Военкоры Русской Весны": -1001355540894,
    "Россия сейчас • Переговоры": -1001650798130,
    "ЭНЕРГОДАРСКИЙ СВЯЗНОЙ": -1001789573966,
    "НАШ Энергодар": -1001575159861,
    "СМИ Россия не Москва": -1001432477212,
    "Запорожская АЭС - Росатом 🇷🇺": -1001454590261,
    "Москва Live": -1001747110091,
    "ЗАЭС. Официально": -1001719529366,
    "ППО ЗАЭС": -1002081177612
}

# 📌 Функция поиска сообщений
def search_messages():
    with TelegramClient("monitoring", API_ID, API_HASH) as client:
        for name, chat_id in CHANNELS.items():
            print(f"🔎 Проверяю канал: {name}")
            for message in client.iter_messages(chat_id, limit=500):  # Проверяем до 500 сообщений
                if message.date:
                    message_date = message.date.replace(tzinfo=timezone.utc)  # Принудительно добавляем UTC
                    if DATE_FROM <= message_date <= DATE_TO:
                        if message.text and KEYWORD.lower() in message.text.lower():  
                            date_str = message_date.strftime("%Y-%m-%d %H:%M:%S")
                            link = f"https://t.me/c/{str(chat_id)[4:]}/{message.id}"
                            print(f"\n📢 Канал: {name}")
                            print(f"🕒 Дата: {date_str}")
                            print(f"💬 Сообщение: {message.text}...")  
                            print(f"🔗 Ссылка: {link}\n")
                            print("---")
# 🚀 Запускаем мониторинг
search_messages()
