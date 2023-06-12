from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text as text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import logging
from config import BOT_TOCKEN


storage = MemoryStorage()
bot = Bot(BOT_TOCKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.DEBUG, filename='bot.log', filemode='w')


class ClientStates(StatesGroup):
    manual = State()
    software = State()
    web = State()
    license = State()
    mfu = State()
    printer = State()
    scaner = State()
    computer = State()
    
    
    


def create_request(flag, message: types.Message):
    print(flag.get())
    if flag.get() != '0':
        if flag == 'scaner':
            message.answer("Заглушка. Создание заявки на сканер")
        elif flag == 'computer':
            message.answer("Заглушка. Создание заявки на компьютер")
        elif flag == 'mfu':
            message.answer("Заглушка. Создание заявки на МФУ")
        elif flag == 'software':
            message.answer("Заглушка. Создание заявки на программное обеспечение")
        elif flag == 'web':
            message.answer("Заглушка. Создание заявки на доступ в интернет")
        elif flag == 'license':
            message.answer("Заглушка. Создание заявки на лицензии")
        elif flag == 'manual':
            message.answer("Заглушка. Создание заявки в IT отдел")
        elif flag == 'printer':
            message.answer("Заглушка. Создание заявки на принтер")
            print(flag) 
        else:
            print("Error")
    else:
        pass



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравствуйте!\nВас привествует бот технической поддержки")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Поиск решения проблемы", "Заявка в IT отдел"]
    keyboard.add(*buttons)
    await message.answer("Выберете режим работы", reply_markup=keyboard)


@dp.message_handler(text(equals="Нет"))
async def process_start_command(message: types.Message,flag):
    path = 'help_resourse/'
    file_name = 'request_manual'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    flag_1 = flag.get()
    create_request(flag_1, message)



@dp.message_handler(text(equals="Да"))
async def process_start_command(message: types.Message):
    path = 'help_resourse/'
    file_name = 'thanks'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    flag = '0'



@dp.message_handler(text(equals="Заявка в IT отдел"))
async def process_start_command(message: types.Message):
    await message.answer("Заглушка. Создание заявки")
    flag = 'manual'






@dp.message_handler(text(equals="Поиск решения проблемы"))
async def process_start_command(message: types.Message):
    #await message.answer("Когда нибудь Миша напишет диплом")
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
    path = 'help_resourse/'
    file_name = 'software'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
    flag = 'software'

@dp.message_handler(text(equals="Проблемы с доступом в интернет"))
async def process_start_command(message: types.Message):
    path = 'help_resourse/'
    file_name = 'web'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
    flag = 'web'

@dp.message_handler(text(equals="Проблемы с лицензиями"))
async def process_start_command(message: types.Message):
    path = 'help_resourse/'
    file_name = 'license'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
    flag = 'license'


@dp.message_handler(text(equals="Принтер"))
async def process_start_command(message: types.Message):
    path = 'help_resourse/'
    file_name = 'printer'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))

@dp.message_handler(text(equals="Сканер"))
async def process_start_command(message: types.Message):
    path = 'help_resourse/'
    file_name = 'scaner'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
    flag = 'scaner'

@dp.message_handler(text(equals="Компьютер"))
async def process_start_command(message: types.Message):
    path = 'help_resourse/'
    file_name = 'computer'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
    flag = 'computer'

@dp.message_handler(text(equals="МФУ"))
async def process_start_command(message: types.Message):
    path = 'help_resourse/'
    file_name = 'mfu'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
    flag = 'mfu'


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)