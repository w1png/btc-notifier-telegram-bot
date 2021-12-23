import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import message, message_entity, message_id, user
from aiogram.types.callback_query import CallbackQuery
from configparser import ConfigParser
import aioschedule
import asyncio
from os import system, name

import markups as mk
import graphs
import price_scraper as ps
import user as usr

system("cls" if name in ("nt", "dos") else "clear")
print("Starting the bot...")

conn = sqlite3.connect('data.db')
c = conn.cursor()
conf = ConfigParser()
conf.read("config.ini", encoding='utf8')

try:
    bot = Bot(token=conf["main_settings"]["token"])
except:
    print("Invalid token!\nYou can change your bot's token using the \"settings.py\" module. Use \"settings.py -h\" for more information.")
    exit(2)
    
dp = Dispatcher(bot)

reminder_time = conf["main_settings"]["time"]

async def send_daily(user_id):
    charts = graphs.Charts()
    await bot.send_photo(
        chat_id=user_id,
        caption=f"Current BTC price is {ps.get_current_price()} USD.",
        photo=charts.daily()
    )

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    user = usr.User(message.chat.id)
    await bot.send_message(
        chat_id=user.get_id(),
        text=f"Hello, {usr.get_user_login(message)}! Use the buttons below to view the current price of BTC or subscribe to a daily price notifier.",
        reply_markup=mk.get_markup_start(user),
    )


@dp.message_handler()
async def message_handler(message: types.Message):
    user = usr.User(message.chat.id)
    if message.text == "Subscribe":
        user.set_subscribed(1)
        await bot.send_message(
            chat_id=user.get_id(),
            text=f"You have been subscibed to the daily notification! The reminder time is {reminder_time} UTC.",
            reply_markup=mk.get_markup_start(user)
        )
    elif message.text == "Unsubscribe":
        user.set_subscribed(0)
        await bot.send_message(
            chat_id=user.get_id(),
            text="You have been unsubscibed from the daily notification!",
            reply_markup=mk.get_markup_start(user)
        )
    elif message.text == "Get current BTC price":
        await send_daily(user.get_id())
    else:
        await bot.send_message(
            chat_id=user.get_id(),
            text="I don't know this command :(\n<i>Contact the developer(@w1png) if you think this is an error.</i>",
            parse_mode="HTML"
        )
        
        
async def send():
    for user in usr.get_notif_list():
        await send_daily(user.get_id())
    
        
async def check_time():
    aioschedule.every().day.at(reminder_time).do(send)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
        
        
async def create_task_startup(x):
    asyncio.create_task(check_time())

        
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=create_task_startup)

