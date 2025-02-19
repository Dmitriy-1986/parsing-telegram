from telethon.sync import TelegramClient

"""
сбора информации о пользователях, которые оставляли комментарии в группе.
"""

# 🔑 Укажи свои API_ID и API_HASH, полученные на my.telegram.org
API_ID = 21002229
API_HASH = 'ef86b3d8721805538b11a9ce26626c91'

GROUP_USERNAME = -1001760516098  # Например: "my_group"

# 📌 Подключаемся к Telegram
client = TelegramClient("session_name", API_ID, API_HASH)

with client:
    users = {}  # Словарь для хранения уникальных пользователей

    # 🔍 Получаем сообщения из группы
    for message in client.iter_messages(GROUP_USERNAME, limit=1000):  # Ограничение в 1000 сообщений
        if message.sender_id and message.sender:
            user = message.sender
            users[user.id] = {
                "id": user.id,
                "имя": user.first_name or "",
                "ник": user.username or "",
                "номер": user.phone or "Скрыт",
            }

    # 📜 Выводим список уникальных пользователей
    for user in users.values():
        print(user)
