# 7727590464:AAEsejDr17HJdzzjnbXoVcE2BM1362_8Xoo

import asyncio
import logging
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

#logging.basicConfig(level=logging.INFO)

bot = Bot(token="7727590464:AAEsejDr17HJdzzjnbXoVcE2BM1362_8Xoo")
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(inline_keyboard=[
        [KeyboardButton(text="Открыть веб-страницу", web_app=WebAppInfo(url='https://mor9q.github.io/telegram-website-store/'))]
    ])

    await message.answer('Привет мой друг!', reply_markup=markup)


@dp.message(lambda msg: msg.web_app_data is not None)
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res['name']}\n Email: {res['email']}\n Phone: {res['phone']}')
    await message.answer('Вы зарегистрировались!')
    

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
