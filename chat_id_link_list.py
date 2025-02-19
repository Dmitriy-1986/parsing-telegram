from telethon import TelegramClient

api_id = 21002229
api_hash = 'ef86b3d8721805538b11a9ce26626c91'
phone_number = '+380936925010'  # Телефон с + в начале

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.connect()

    if not await client.is_user_authorized():
        print("Требуется авторизация. Введите код из Telegram.")
        await client.send_code_request(phone_number)
        code = input("Введите код: ")  # Ожидаем код от пользователя
        await client.sign_in(phone_number, code)

    dialogs = await client.get_dialogs()
    print("Ваши чаты и ID:")
    for dialog in dialogs:
        chat_id = dialog.id
        chat_title = dialog.name
        chat_username = dialog.entity.username if dialog.entity and hasattr(dialog.entity, 'username') else None
        
        if chat_username:
            chat_link = f"https://t.me/{chat_username}"
        else:
            chat_link = "Нет ссылки"

        print(f"{chat_title}: {chat_id} ({chat_link})")

    await client.disconnect()

import asyncio
asyncio.run(main())
