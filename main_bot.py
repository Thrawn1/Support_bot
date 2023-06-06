from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text as text
import logging

BOT_TOCKEN = '5826823154:AAHqFoWizQ2dF0YU4twnmo2JdagEZ24ztvU'

bot = Bot(BOT_TOCKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(text(equals="Поиск решения проблемы"))
async def process_start_command(message: types.Message):
    await message.answer("Когда нибудь Миша напишет диплом")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Не работоспобность обрудования", "Проблемы с программным обеспечением", "Проблемы с доступом в интернет", "Проблемы с лицензиями"]
    keyboard.add(*buttons)  
    await message.answer("Выберете категорию проблемы", reply_markup=keyboard)

@dp.message_handler(text(equals="Не работоспобность обрудования"))
async def process_start_command(message: types.Message):
    await message.answer("Заглушка. Не работоспобность обрудования")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Принтер", "Компьютер", "Сканер", "МФУ"]
    keyboard.add(*buttons)  
    await message.answer("Выберете подкатегорию проблемы", reply_markup=keyboard)

@dp.message_handler(text(equals="Проблемы с программным обеспечением"))
async def process_start_command(message: types.Message):
    await message.answer("Заглушка. Проблемы с программным обеспечением")

@dp.message_handler(text(equals="Проблемы с доступом в интернет"))
async def process_start_command(message: types.Message):
    await message.answer("Заглушка. Проблемы с доступом в интернет")

@dp.message_handler(text(equals="Проблемы с лицензиями"))
async def process_start_command(message: types.Message):
    await message.answer("Заглушка. Проблемы с лицензиями")


@dp.message_handler(text(equals="Заявка в IT отдел"))
async def process_start_command(message: types.Message):
    await message.answer("Заглушка. Создание заявки")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравствуйте!\nВас привествует бот технической поддержки")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Поиск решения проблемы", "Заявка в IT отдел"]
    keyboard.add(*buttons)
    await message.answer("Выберете режим работы", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
