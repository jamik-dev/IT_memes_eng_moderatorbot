import logging

from aiogram import types
from data.config import CHANNELS
from loader import bot, dp
from data.config import ADMINS


@dp.message_handler(commands=['start'], user_id=ADMINS[0])
async def show_channels(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nBiz sizni uzoq kutgan edik")


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nBotni ishga tushirish uchun <b><a href='https://t.me/web_developer_OIK'>Admin</a></b>ga murojat qiling!")
