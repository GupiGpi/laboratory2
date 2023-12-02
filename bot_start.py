from aiogram.filters import CommandStart
from aiogram import types, Router
from loader import dp
from aiogram.utils.markdown import hbold

start_router=Router()

@start_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}')
    kb=[
        [types.KeyboardButton(text='Я робот'),
         types.KeyboardButton(text='Я не робот')],
        [types.KeyboardButton(text='Робот, но мне сказали что я не робот')]
    ]

    keyBoard=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='Введите любой текст')

    await message.answer(f'Привет, путник,{message.from_user.full_name}!', reply_markup=keyBoard)
