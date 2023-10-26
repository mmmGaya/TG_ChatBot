from create_bot import dp, bot
from aiogram import types
from dialog_db import create_db
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

ID = None


class FSMAdmin(StatesGroup):
    group = State()
    time = State()
    mess = State()
    


@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def check_admin(message:types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Вы вошли в админ-панель ^.^')
    await message.delete()


@dp.message_handler(commands='Изменить', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.group.set()
        await message.reply('Введите группу: ')


@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel(message:types.Message, state:FSMContext):
    cur_state = await state.get_state()
    if cur_state is None:
        return
    await state.finish()
    await message.reply('Все ваши действия были отменены ^.^')



@dp.message_handler(state=FSMAdmin.group)
async def select_group(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['group'] = message.text.lower()
        await FSMAdmin.next()
        await message.reply('Введите дату когда пара будет изменена: (Х сентября)')



@dp.message_handler(state=FSMAdmin.time)
async def inp_datatime(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['time'] = message.text
        await FSMAdmin.next()
        await message.reply(f'Введите сообщени для группы: ')

@dp.message_handler(state=FSMAdmin.mess)
async def add_message(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['message'] = message.text
            all_users = create_db.select_groups(data['group'])
            if all_users:
                for user in all_users:
                    try:
                        await bot.send_message(user, f'{data["time"]}\n{data["group"]}\n{data["message"]}' )
                    except:
                        print('Произошла ошибка рассылки')
                await message.reply("Сообщение успешно разослано ^.^")
            else:
                await message.reply("Нет зарегистрированных пользователей данной группы ^.^")
        await state.finish()





def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(check_admin, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(cm_start, commands='Изменить', state=None)
    dp.register_message_handler(select_group, state=FSMAdmin.group)
    dp.register_message_handler(inp_datatime, state=FSMAdmin.time)
    dp.register_message_handler(add_message, state=FSMAdmin.mess)


    