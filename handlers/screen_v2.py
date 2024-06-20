from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import re

from states.screenv2_states import screenv2_states
from dispatcher import dp, bot
from aiogram import types
from aiogram.types.input_file import InputFile
from aiogram.dispatcher.filters import Text
from main.screenv2 import DrawScreen2
from main.users import Users
import logging 


DrawScreen = DrawScreen2()
Users = Users()

list_button_name = ['Сделать скрин', '🚨 Инфо']
list_of_birges = ['BingX', 'Binance']
keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
keyboard.add(*list_button_name)
markup = keyboard
keyboardofbirges = types.ReplyKeyboardMarkup(resize_keyboard= True)
keyboardofbirges.add(*list_of_birges)



@dp.message_handler(Text(equals='Сделать скрин (расширенный)'))
@dp.message_handler(Command('make_screen_v2'))
async def main(message: types.Message):
    if Users.check_is_paid(message.from_user.username): 
        await message.answer('Введите название монеты', reply_markup=markup)
        await screenv2_states.Q1.set()
    else:
        await message.answer('У вас нет доступа, обратитесь к @s_ryzeee')
    
@dp.message_handler(state=screenv2_states.Q1)
async def main(message: types.Message, state: FSMContext):
    answer = message.text
    if len(answer) > 10:
        await state.finish()
        await message.answer('Слишком большое название')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(coin_name = answer)
        await message.answer('Введите тип, например "Long" или "Short"')
        await screenv2_states.next()


@dp.message_handler(state=screenv2_states.Q2)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if answer != 'long' and answer != "short":
        await state.finish()
        await message.answer(f'Ошибка, нужно ввести "Long" или "Short"')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(type = answer)
        await message.answer('Введите размер плеча, например "20" ')
        await screenv2_states.next()

@dp.message_handler(state=screenv2_states.Q3)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if len(answer) > 5 or not(answer.isdigit()):
        await state.finish()
        await message.answer(f'Ошибка, плечо нужно выразить только числами. А также оно не должно быть слишком большое или маленькое')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(leverage = answer)
        await message.answer('Введите маржу, например "20" ')
        await screenv2_states.next()

@dp.message_handler(state=screenv2_states.Q4)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if not(DrawScreen.is_number(answer)):
        await state.finish()
        await message.answer(f'Ошибка, маржа должна быть числом')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(marge = answer)
        await message.answer('Введите цену входа(entry price), например "1566" ')
        await screenv2_states.next()

@dp.message_handler(state=screenv2_states.Q5)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if not(DrawScreen.is_number(answer)):
        await state.finish()
        await message.answer(f'Ошибка, цена должна состоять только из цифр')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(entry_price =answer)
        await message.answer('Введите текущую цену(current price), например "2477" ')
        await screenv2_states.next()


@dp.message_handler(state=screenv2_states.Q6)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if not(DrawScreen.is_number(answer)):
        await state.finish()
        await message.answer(f'Ошибка, цена должна состоять только из цифр')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(current_price =answer)
        await message.answer('Введите, отображаемый риск (без процентов в конце)', reply_markup=markup)
        await screenv2_states.next()

@dp.message_handler(state = screenv2_states.Q7)
async def main(message: types.Message, state: FSMContext):

    answer = message.text.lstrip().lower()
    if (DrawScreen.is_number(answer)):
        await state.update_data(risk =answer)
        data = await state.get_data()
        await state.finish()
        await message.answer('Подождите чуток', reply_markup=markup)
        
        DrawScreen.drawscreen(data, message.from_user.id)
        
        photo = InputFile(f"main/images/{message.from_user.id}_img.jpg")
        await bot.send_photo(message.from_user.id, photo, reply_markup=markup)
        DrawScreen.delete_screen(chat_id=message.from_user.id)
    else: 
        await bot.send_message(chat_id=message.from_user.id, text = 'Ошибка, ответ неверный')
        await bot.send_message(chat_id=message.from_user.id, text = f'Повторить попытку: /make_screen', reply_markup=markup)

    

    



