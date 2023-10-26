from aiogram import types
from aiogram.dispatcher import Dispatcher
from ai_model import collect_messages
from dialog_db import create_db
from create_bot import dp, bot


# @dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, f'Привет, Я бот-координатор РУКСИ. Я знаю о РКСИ все ну или почти всё. Чтобы в этом убедится задай мне вопрос ^.^ ')


# @dp.message_handler(commands=['Расписание'])
async def command_shedule(message : types.Message):
    await bot.send_message(message.from_user.id, f'Вот раписание!!!!')


# @dp.message_handler()
async def command_gpt(message : types.Message):
    await bot.send_message(message.from_user.id, '⌛️Ваш запрос обрабатывается подождите немного ^.^ ')
    response = collect_messages(message.text) 
    await bot.send_message(message.from_user.id, response)   
    await create_db.insert_data((message.from_user.username, message.text, response))


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_shedule, commands=['Расписание'])
    dp.register_message_handler(command_gpt)


