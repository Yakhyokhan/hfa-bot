from aiogram import types
from loader import dp, bot_name
from data.config import confirmatives, errorgr_id


@dp.callback_query_handler(user_id = confirmatives, text = 'conf')
async def confirm(call: types.CallbackQuery):
    text = call.message.text
    text = '#тасдиқланди ✅✅✅\n\n' + text
    await call.message.edit_text(text)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(user_id = confirmatives, text = 'ref')
async def refuse(call: types.CallbackQuery):
    text = call.message.text
    text = '#рад_этилди ❌❌❌\n\n' + text
    await dp.bot.send_message(errorgr_id, text)
    await call.message.delete()
    await call.answer(cache_time=60)
    