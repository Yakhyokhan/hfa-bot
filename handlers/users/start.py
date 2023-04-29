from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import bot_name
from loader import dp
from filters.private import IsPrivateChat

@dp.message_handler(IsPrivateChat(),CommandStart())
async def bot_start(message: types.Message):
    tid = message.from_user.id
    username = message.from_user.username
    username = '@' + username if username else message.from_user.full_name
    await message.answer(f"Salom, {username}!\n<b>{bot_name}</b>ga hush kelibsiz\n\nO'zingiz yoqtirgan tiktok yoki instagram video/rasm linkini tashlang")
