from telethon import TelegramClient

api_id = *****
api_hash = '*****'
phone_number = '*****'  # Телефон с + в начале

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
        print(f"{dialog.name}: {dialog.id}")

    await client.disconnect()

import asyncio
asyncio.run(main())

