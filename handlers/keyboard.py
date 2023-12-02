from aiogram import types, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_router=Router()
@kb_router.message(Command('keyboard'))
async def reply_keyboard_gen(message: types.Message):
    builder=ReplyKeyboardBuilder()
    for i in range(1,17):
        builder.add(types.KeybordButton(text=str(i)))
        builder.adjust(4)
    await message.answer('Выберите кнопку:',reply_markup=builder.as_markup(resize_keyboard=True))
