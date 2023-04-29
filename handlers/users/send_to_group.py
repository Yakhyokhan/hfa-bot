from aiogram import types
from data.config import group_id, senders
from loader import dp
from keyboards.inline.for_check import for_check
from filters.private import IsPrivateChat
from add_tools.alph_chancher import latin_to_krill


@dp.message_handler(IsPrivateChat(),chat_id = senders)
async def bot_start(msg: types.Message):
    text = msg.text
    text = latin_to_krill(text)
    await dp.bot.send_message(group_id, text, reply_markup=for_check)
    