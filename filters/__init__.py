from aiogram import Dispatcher

from loader import dp
from .private import IsPrivateChat


if __name__ == "filters":
    dp.filters_factory.bind(IsPrivateChat)
