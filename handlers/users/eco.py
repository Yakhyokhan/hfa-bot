from time import sleep
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private import IsPrivateChat
from loader import dp


@dp.message_handler(text='/err')
async def bot_start(message: types.Message):
    username = message.from_user.username
    username = '@' + username if username else message.from_user.full_name
    await message.answer(message)