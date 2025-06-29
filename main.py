import os
import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("❌ BOT_TOKEN не найден в переменных окружения!")
    exit(1)

print("✅ BOT_TOKEN загружен. Запускаем бота...")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("✅ Вы подписались на уведомления")

async def main():
    try:
        await dp.start_polling()
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    asyncio.run(main())
