from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from dispatcher import dp
from aiogram import types


@dp.message_handler(Command('start'))
async def on_start_test(message: types.Message):
    list_button_name = ['Сделать скрин (обычный)', 'Сделать скрин (расширенный)', '🚨 Инфо']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
    keyboard.add(*list_button_name)
    await message.answer('Привет, ' + str(message.from_user.full_name) + '❤️\nЭто бот для генерации скриншотов с профитами с биржи Binance и Bingx 📈 \n❗️ Просто напиши /make_screen или /make_screen_v2 - для расширенных скринов', reply_markup=keyboard)
    