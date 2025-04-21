
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Здравствуйте! Я Юридический бот. Задайте свой вопрос.")

@dp.message_handler()
async def handle_message(message: types.Message):
    await message.answer("Ваш вопрос принят. Ответ скоро появится.")

if __name__ == "__main__":
    executor.start_polling(dp)
