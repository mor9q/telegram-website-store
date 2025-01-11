# 7727590464:AAEsejDr17HJdzzjnbXoVcE2BM1362_8Xoo

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

#logging.basicConfig(level=logging.INFO)

bot = Bot(token="7727590464:AAEsejDr17HJdzzjnbXoVcE2BM1362_8Xoo")
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Открыть веб-страницу', url='https://mor9q.github.io/telegram-website-store/'))

    await message.answer('Привет мой друг!', reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
