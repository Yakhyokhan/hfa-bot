from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

for_check = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'тасдиқлаш', callback_data = 'conf'),
            InlineKeyboardButton(text = 'рад этиш', callback_data = 'ref')
        ]
    ]
)