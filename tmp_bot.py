from aiogram import Bot, Dispatcher, executor, types
import asyncio
BOT_TOCKEN = '5826823154:AAHqFoWizQ2dF0YU4twnmo2JdagEZ24ztvU'
# Объект бота

bot = Bot(BOT_TOCKEN)
# Диспетчер для бота
dp = Dispatcher(bot)

# Приветственное сообщение при старте бота
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравствуйте!\nВас привествует бот технической поддержки")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Поиск решения проблемы", "Заявка в IT отдел",]
    keyboard.add(*buttons)  
    await message.answer("Выберете режим работы", reply_markup=keyboard)
    #Если выбран режим поиска решения проблемы, то пользователю предлагается выбрать категорию проблемы
    #Категории проблем : 1. Не работоспобность обрудования 2. Проблемы с программным обеспечением 3. Проблемы с доступом в интернет 4. Проблемы с лицензиями
    @dp.message_handler()
    async def process_start_command(message: types.Message):
        if message.text == "Поиск решения проблемы":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Не работоспобность обрудования", "Проблемы с программным обеспечением", "Проблемы с доступом в интернет", "Проблемы с лицензиями"]
            keyboard.add(*buttons)  
            await message.answer("Выберете категорию проблемы", reply_markup=keyboard)
            #Если выбрана категория проблемы, то пользователю предлагается выбрать подкатегорию проблемы
            #Подкатегории проблем : 1. Не работоспобность обрудования 2. Проблемы с программным обеспечением 3. Проблемы с доступом в интернет 4. Проблемы с лицензиями
            @dp.message_handler()
            async def process_start_command(message: types.Message):
                if message.text == "Не работоспобность обрудования":
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    buttons = ["Принтер", "Компьютер", "Сканер", "МФУ"]
                    keyboard.add(*buttons)  
                    await message.answer("Выберете подкатегорию проблемы", reply_markup=keyboard)
                    #Если выбрана подкатегория проблемы, то пользователю предлагается выбрать проблему
                    #Проблемы : 1. Не работоспобность обрудования 2. Проблемы с программным обеспечением 3. Проблемы с доступом в интернет 4. Проблемы с лицензиями
                    @dp.message_handler()
                    async def process_start_command(message: types.Message):
                        if message.text == "Принтер":
                            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            buttons = ["Принтер не печатает", "Принтер не сканирует", "Принтер не копирует", "Принтер не подключается"]
                            keyboard.add(*buttons)
                            await message.answer("Выберете проблему", reply_markup=keyboard)
                            #Если выбрана проблема, то пользователю предлагается выбрать решение
                            #Решения : 1. Не работоспобность обрудования 2. Проблемы с программным обеспечением 3. Проблемы с доступом в интернет 4. Проблемы с лицензиями
                            @dp.message_handler()
                            async def process_start_command(message: types.Message):
                                if message.text == "Принтер не печатает":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                                if message.text == "Принтер не сканирует":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                                if message.text == "Принтер не копирует":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                                if message.text == "Принтер не подключается":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                        if message.text == "Компьютер":
                            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            buttons = ["Компьютер не включается", "Компьютер не подключается к интернету", "Компьютер не подключается к принтеру", "Компьютер не подключается к сканеру"]
                            keyboard.add(*buttons)
                            await message.answer("Выберете проблему", reply_markup=keyboard)
                            #Если выбрана проблема, то пользователю предлагается выбрать решение
                            #Решения : 1. Не работоспобность обрудования 2. Проблемы с программным обеспечением 3. Проблемы с доступом в интернет 4. Проблемы с лицензиями
                            @dp.message_handler()
                            async def process_start_command(message: types.Message):
                                if message.text == "Компьютер не включается":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                                if message.text == "Компьютер не подключается к интернету":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                                if message.text == "Компьютер не подключается к принтеру":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                                if message.text == "Компьютер не подключается к сканеру":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
                        if message.text == "Лицензии":
                            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            buttons = ["Проблемы с лицензиями", "Проблемы с лицензиями", "Проблемы с лицензиями", "Проблемы с лицензиями"]
                            keyboard.add(*buttons)
                            await message.answer("Выберете проблему", reply_markup=keyboard)
                            #Если выбрана проблема, то пользователю предлагается выбрать решение
                            #Решения : 1. Не работоспобность обрудования 2. Проблемы с программным обеспечением 3. Проблемы с доступом в интернет 4. Проблемы с лицензиями
                            @dp.message_handler()
                            async def process_start_command(message: types.Message):
                                if message.text == "Проблемы с лицензиями":
                                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    buttons = ["Проверьте подключение к сети", "Проверьте подключение к компьютеру", "Проверьте наличие бумаги", "Проверьте наличие чернил"]
                                    keyboard.add(*buttons)
                                    await message.answer("Выберете решение", reply_markup=keyboard)
        else:
                await message.answer("Вы не выбрали категорию")
            


#Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)