from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from ai_model import collect_messages
from dialog_db import create_db


#------Create Bot--------
bot = Bot(token=os.getenv('BOT'))
dp = Dispatcher(bot)

# -----Connect to DB--------
create_db.connect_to_database()




@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, f'Привет, Я бот-координатор РУКСИ. Я знаю о РКСИ все ну или почти всё. Чтобы в этом убедится задай мне вопрос ^.^ ')


@dp.message_handler(commands=['Расписание'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, f'Вот раписание!!!!')


@dp.message_handler()
async def command_gpt(message : types.Message):
    await bot.send_message(message.from_user.id, '⌛️Ваш запрос обрабатывается подождите немного ^.^ ')
    response = collect_messages(message.text) 
    await bot.send_message(message.from_user.id, response)   
    await create_db.insert_data((message.from_user.username, message.text, response))



executor.start_polling(dp, skip_updates=True)




