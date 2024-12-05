from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands=['start'])
async def start_message(message):
    # print('Start message')
    await message.answer('Привет! Я бот помогающий  твоему здоровью')


@dp.message_handler()  #этот хендлер лучше ставить в самый конец, иначе он будет перехватывать все остальные
async def all_messages(message):
    print('Получено новое сообщение')
    await message.answer('Введите команду \start, чтобы начать общение')






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)