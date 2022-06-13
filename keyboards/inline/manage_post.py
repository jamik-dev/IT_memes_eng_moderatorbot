from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Chop etish", callback_data="post"),
        InlineKeyboardButton(text="❌ Rad etish", callback_data="cancel"),
    ]]
)
share = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Join Us 👥",url="https://t.me/jamshid_dev", callback_data="share")
        ]
    ]   
)
