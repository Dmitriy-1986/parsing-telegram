from telethon import TelegramClient

# Замените на ваш api_id и api_hash
api_id = 21002229
api_hash = 'ef86b3d8721805538b11a9ce26626c91'

# Замените на ваш номер телефона
phone_number = '+380936925010'

# Username канала/группы
group_username = -1001784427002 

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    
    # Авторизация через телефон
    await client.start(phone_number)

    try:
        # Получаем участников группы (если это публичная группа и вы в ней)
        participants = await client.get_participants(group_username)
        
        # Открываем файл для записи
        with open('participants.txt', 'w', encoding='utf-8') as f:
            # Записываем заголовок
            f.write("+-------------------------------------------------------+\n")
            f.write("ID,     Имя,     Имя пользователя,     Номер телефона\n")
            f.write("+-------------------------------------------------------+\n")
            
            # Записываем информацию о пользователях
            for participant in participants:
                username = f"@{participant.username}" if participant.username else 'Нет ника'
                first_name = participant.first_name if participant.first_name else 'Без имени'
                phone = participant.phone if participant.phone else 'Нет телефона'
                f.write(f"{participant.id}, {first_name}, {username}, {phone}\n")
        
        print("Информация о пользователях записана в файл 'participants.txt'")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Завершаем работу с клиентом
        await client.disconnect()

# Запуск асинхронной функции
import asyncio
asyncio.run(main())
