import logging
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard
from loader import dp, bot
from utils.memes_api import memes_api   


@dp.message_handler(Command("new_post"), user_id=ADMINS[0])
async def create_post(message: Message):
    await message.answer("<i>Sizga bir qancha rasmlar yuborilyapti . . .</i>")
    response = memes_api()
    for image in response:
        index = response.index(image)
        await dp.bot.send_photo(ADMINS[0] ,image, caption=f"{index + 1}chi rasm", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(text="post")
async def approve_post(call: CallbackQuery):
    await call.answer("Chop etishga ruhsat berdingiz.", show_alert=True)
    target_channel = CHANNELS[0]
    image = call.message.photo[-1]
    # response = likedFunc(image)

    # if response == "full":
    #     await call.message.answer(f"1 kunlik reja to'la!\n{likedMeme}")
    #     tz_UZ = pytz.timezone('Asia/Tashkent') 
    #     hour = datetime.now(tz_UZ).strftime("%H")
    #     minute = datetime.now(tz_UZ).strftime("%M")
    #     for obj in likedMeme:
    #         if int(hour)>=0 and int(hour) <= 6:
    #             while "0600" != hour+minute:
    #                 x = int(hour)*60 + int(minute)
    #                 y = 360
    #                 z = y-x
    #                 time.sleep(z)


    await call.message.edit_reply_markup()
    await dp.bot.send_photo(photo = image.file_id, chat_id=target_channel, caption=f"<i><b>The world of memes in English</b></i>\n\n<code>Share with your friends๐</code>\n\n๐ <b><a href='https://t.me/IT_memes_eng'>Telegram</a></b> ๐")
    await call.answer(cache_time=60)


# disable_webpage_preview = True , messages not photos

@dp.callback_query_handler(text="cancel")
async def decline_post(call: CallbackQuery):
    await call.answer("Post rad etildi.", show_alert=True)
    await call.message.delete()
    await call.answer(cache_time=60)