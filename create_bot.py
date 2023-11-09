from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

storage = MemoryStorage() 
bot = Bot(token=os.getenv('BOT'))

dp = Dispatcher(bot, storage=storage)