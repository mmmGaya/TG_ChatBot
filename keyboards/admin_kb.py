from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Написать')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(b1)