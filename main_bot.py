from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text as text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import logging
from config import BOT_TOCKEN


storage = MemoryStorage()
bot = Bot(BOT_TOCKEN)
dp = Dispatcher(bot=bot, storage=storage)
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='w')


class ClientStates(StatesGroup):
    manual = State()
    software = State()
    web = State()
    license = State()
    mfu = State()
    printer = State()
    scaner = State()
    computer = State()
    choice_main = State()
    choice_problem = State()
    
    
def keyboard_main_menu() -> ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Поиск решения проблемы", "Заявка в IT отдел"]
    keyboard.add(*buttons)
    return keyboard

def keyboard_yes_no() -> ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да", "Нет"]
    keyboard.add(*buttons)
    return keyboard

def keyboard_problem() -> ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Не работоспобность обрудования", "Проблемы с программным обеспечением", "Проблемы с доступом в интернет", "Проблемы с лицензиями"]
    keyboard.add(*buttons)
    return keyboard

def keyboard_equipment() -> ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Принтер", "Сканер", "Компьютер", "МФУ"]
    keyboard.add(*buttons)
    return keyboard

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравствуйте!\nВас привествует бот технической поддержки",reply_markup=keyboard_main_menu())
    await message.answer("Выберете режим работы")
    await ClientStates.choice_main.set()


@dp.message_handler(text(equals="Нет"))
async def slect_no(message: types.Message):
    await ClientStates.manual.set()
    await create_manual_request(message)
    


@dp.message_handler(text(equals="Да"))
async def process_end(message: types.Message, state: FSMContext):
    path = 'help_resourse/'
    file_name = 'thanks'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await state.finish()



@dp.message_handler(text(equals="Заявка в IT отдел"))
async def create_manual_request(message: types.Message):
    path = 'help_resourse/'
    file_name = 'request_manual'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Отмена"]
    keyboard.add(*buttons)


@dp.message_handler(text(equals="Отмена"))
async def process_cancel(message: types.Message, state: FSMContext):
    path = 'help_resourse/'
    file_name = 'thanks'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await state.finish()


@dp.message_handler(text(equals="Поиск решения проблемы"), state = ClientStates.choice_main)
async def process_select_problem(message: types.Message, state: FSMContext):
    #await message.answer("Когда нибудь Миша напишет диплом")
    await message.answer("Выберете категорию проблемы", reply_markup=keyboard_problem())
    await ClientStates.next()


@dp.message_handler(text(equals="Не работоспобность обрудования"))
async def process_select_equipment(message: types.Message):
    await message.answer("Выберете подкатегорию проблемы", reply_markup=keyboard_equipment())


@dp.message_handler(text(equals="Проблемы с программным обеспечением"))
async def software_problem(message: types.Message):
    path = 'help_resourse/'
    file_name = 'software'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=keyboard_yes_no())


@dp.message_handler(text(equals="Проблемы с доступом в интернет"))
async def web_problem(message: types.Message):
    path = 'help_resourse/'
    file_name = 'web'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=keyboard_yes_no())


@dp.message_handler(text(equals="Проблемы с лицензиями"))
async def license_problem(message: types.Message):
    path = 'help_resourse/'
    file_name = 'license'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=keyboard_yes_no())


@dp.message_handler(text(equals="Принтер"))
async def printer_problem(message: types.Message):
    path = 'help_resourse/'
    file_name = 'printer'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=keyboard_yes_no())

@dp.message_handler(text(equals="Сканер"))
async def scaner_problem(message: types.Message):
    path = 'help_resourse/'
    file_name = 'scaner'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=keyboard_yes_no())

@dp.message_handler(text(equals="Компьютер"))
async def computer_problem(message: types.Message):
    path = 'help_resourse/'
    file_name = 'computer'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=keyboard_yes_no())

@dp.message_handler(text(equals="МФУ"))
async def mfu_problem(message: types.Message):
    path = 'help_resourse/'
    file_name = 'mfu'
    print(path + file_name)
    with open((path + file_name), 'r',encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer("Данная информация помогла вам?", reply_markup=keyboard_yes_no())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)