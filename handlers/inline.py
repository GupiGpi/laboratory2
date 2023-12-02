from aiogram import types, Bot, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_router=Router()
@inline_router.message(Command('Inline'))
async def cmd_inline(message:types.Message, bot: Bot):
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='Google',
        url='https://google.com')
    )
    builer.row(types.InlineKeyboardButton(
        text='Github',
        url='https://github.com')
    )

    builder.row(types.InlineKeyboardButton(
        text='Youtube',
        url='https://youtube.com')
    )
    await message.answer(
        'Выберите ссылку', reply_marker=builder.as_markup(),
    )
