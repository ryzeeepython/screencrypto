from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import re
from states.make_screen_states import make_screen_states
from dispatcher import dp, bot
from aiogram import types
from aiogram.types.input_file import InputFile
from aiogram.dispatcher.filters import Text
from main.main import DrawScreen, DrawScreen_Bingx
from main.users import Users
import logging 


DrawScreen = DrawScreen()
DrawScreen_Bingx = DrawScreen_Bingx()
Users = Users()

list_button_name = ['Сделать скрин(обычный)', 'Сделать скрин (расширенный)', '🚨 Инфо']
list_of_birges = ['BingX', 'Binance']
keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
keyboard.add(*list_button_name)
markup = keyboard
keyboardofbirges = types.ReplyKeyboardMarkup(resize_keyboard= True)
keyboardofbirges.add(*list_of_birges)
#клава для выбора типа вывода прибыли
inline_btn_1 = InlineKeyboardButton('В процентах (ROI)', callback_data='В процентах (ROI)')
inline_btn_2 = InlineKeyboardButton('В USDT(PNL)', callback_data='В USDT(PNL)')

inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb1.add(inline_btn_2)


@dp.message_handler(Text(equals='Сделать скрин (обычный)'))
@dp.message_handler(Command('make_screen'))
async def main(message: types.Message):
    if Users.check_is_paid(message.from_user.username): 
        await message.answer('Введите название монеты', reply_markup=markup)
        await make_screen_states.Q1.set()
    else:
        await message.answer('У вас нет доступа, обратитесь к @s_ryzeee')
    

@dp.message_handler(state=make_screen_states.Q1)
async def main(message: types.Message, state: FSMContext):
    answer = message.text
    if len(answer) > 10:
        await state.finish()
        await message.answer('Слишком большое название')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(birga ='BingX')
        await state.update_data(pair =answer)
        await message.answer('Введите тип, например "Long" или "Short"')
        await make_screen_states.next()



@dp.message_handler(state=make_screen_states.Q2)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if answer != 'long' and answer != "short":
        await state.finish()
        await message.answer(f'Ошибка, нужно ввести "Long" или "Short"')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(type =answer)
        await message.answer('Введите размер плеча, например "20" ')
        await make_screen_states.next()

@dp.message_handler(state=make_screen_states.Q3)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if len(answer) > 5 or not(answer.isdigit()):
        await state.finish()
        await message.answer(f'Ошибка, плечо нужно выразить только числами. А также оно не должно быть слишком большое или маленькое')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(leverage =answer)
        await message.answer('Введите маржу, например "20" ')
        await make_screen_states.next()

@dp.message_handler(state=make_screen_states.Q4)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if len(answer) > 5 or not(answer.isdigit()):
        await state.finish()
        await message.answer(f'Ошибка, плечо нужно выразить только числами. А также оно не должно быть слишком большое или маленькое')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(position = answer)
        await message.answer('Введите цену входа(entry price), например "1566" ')
        await make_screen_states.next()

@dp.message_handler(state=make_screen_states.Q5)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if not(DrawScreen.is_number(answer)):
        await state.finish()
        await message.answer(f'Ошибка, цена должна состоять только из цифр')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(entry_price =answer)
        await message.answer('Введите текущую цену(current price), например "2477" ')
        await make_screen_states.next()


@dp.message_handler(state=make_screen_states.Q6)
async def main(message: types.Message, state: FSMContext):
    answer = message.text.lstrip().lower()
    if not(DrawScreen.is_number(answer)):
        await state.finish()
        await message.answer(f'Ошибка, цена должна состоять только из цифр')
        await message.answer(f'Повторить попытку: /make_screen', reply_markup=markup)
    else:
        await state.update_data(current_price = answer)
        data = await state.get_data()
        await state.finish()
        await bot.send_message(chat_id=message.from_user.id, text = 'Подождите чуток')
        if data["birga"] == "BingX":
            DrawScreen_Bingx.drawscreen_test(data, message.from_user.id)
        else: 
            DrawScreen.drawscreen(data, message.from_user.id)
        photo = InputFile(f"main/images/{message.from_user.id}_img.jpg")
        await bot.send_photo(message.from_user.id, photo, reply_markup=markup)
        DrawScreen.delete_screen(chat_id=message.from_user.id)
        await bot.send_message(text=f'{message.from_user.full_name} сделал скрин', chat_id=631694976)


    



