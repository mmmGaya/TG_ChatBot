from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('BOT'))
# bot = Bot('6064761154:AAHpetSzNO5SEqNGfrZbph7vBErsWPn9TFQ')
dp = Dispatcher(bot)