from aiogram import types
from aiogram.types.callback_query import CallbackQuery

def get_markup_start(user):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(text="Unsubscribe" if user.is_subscribed() else "Subscribe"))
    markup.add(types.KeyboardButton(text="Get current BTC price"))
    return markup