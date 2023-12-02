from random import randint

from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

random_router=Router()

@random_router.message(Command('random'))
async def cmd_random(message:types.Message):
    builder=InlineKeyboardBuilder()
    builer.row(types.InlineKeyboardButton(
        text='нажми на меня', callback_data='Click')
    )
    await message.answer('Нажми для генерации случайного число от 1 до 100:',reply_markup=builder.anser)

@random_router.callback_query(F.data=='Click')
async def generation_random(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1,100)))
    await callback.answer()
