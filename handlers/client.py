from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from ai_model import collect_messages
from dialog_db import create_db
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards import kb_client 




async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, f'Привет, Я бот-координатор РУКСИ. Я знаю о РКСИ все ну или почти всё. Чтобы в этом убедиться задай мне вопрос ^.^ ', reply_markup=kb_client)



class FSMClient(StatesGroup):
    register = State()
    schedule = State()


async def command_sсhedule(message : types.Message):
    if not create_db.check_user(message.from_user.id):
        await FSMClient.register.set()
        await message.reply("Происходит регистрация, пожалуйста введите свою группу ^.^")
    else:
        await FSMClient.schedule.set()
        await message.reply("Введите номер группы или ФИО преподавателя, чтобы получить расписание. Если вы вдруг передумали идти в колледже, напишите 'отмена' ")

# @dp.message_handler(state=FSMClient.register)
async def register_user(message : types.Message, state:FSMContext):
    create_db.register_user((message.from_user.id, message.from_user.username, message.text.lower())) 
    await FSMClient.next()
    await message.reply("Вы успешно зареганы!!! Чтобы получить расписание введите номер группы или ФИО преподавателя ^.^ ")


async def show_schedule(message : types.Message, state:FSMContext):
    response = f'{message.text}- sdfghjkl'
    await bot.send_message(message.from_user.id, message.text)
    await state.finish()  


@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel(message:types.Message, state:FSMContext):
    cur_state = await state.get_state()
    if cur_state is None:
        return
    await state.finish()
    await message.reply('Как скажите ^.^')

    
async def command_gpt(message : types.Message):
    await bot.send_message(message.from_user.id, '⌛️Ваш запрос обрабатывается подождите немного ^.^ ')
    response = collect_messages(message.text) 
    await bot.send_message(message.from_user.id, response)   
    await create_db.insert_data((message.from_user.username, message.text, response))


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_sсhedule, commands=['Расписание'], state=None)
    dp.register_message_handler(register_user, state=FSMClient.register)
    dp.register_message_handler(show_schedule, state=FSMClient.schedule)
    dp.register_message_handler(cancel, state="*", commands='отмена')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(command_gpt)


