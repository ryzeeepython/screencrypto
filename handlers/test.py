from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from states.test_state import test_states
from dispatcher import dp, bot
from aiogram import types
from main.main import DrawScreen, DrawScreen_Bingx
from main.users import Users
from aiogram.types.input_file import InputFile

DrawScreen = DrawScreen()
DrawScreen_Bingx = DrawScreen_Bingx()
Users = Users()



@dp.message_handler(Command('test'))
async def on_start_test(message: types.Message):

    await message.answer('Введи res')
    await test_states.Q1.set()

@dp.message_handler(state=test_states.Q1)
async def on_start_test(message: types.Message, state: FSMContext):
    res = message.text
    await state.finish()
    DrawScreen_Bingx.drawscreen_test(res, message.chat.id)
    photo = InputFile(f"main/images/{message.chat.id}_img.jpg")  
    await bot.send_photo(message.chat.id, photo)
    DrawScreen.delete_screen(chat_id=message.chat.id)
