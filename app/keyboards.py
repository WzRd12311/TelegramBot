from aiogram.types import ReplyKeyboardMarkup as RKM
from aiogram.types import KeyboardButton as KB

main_menu = RKM(keyboard=[[KB(text='Show Photo'), KB(text='Show Quiz')], [KB(text='Show Git Hub')]], resize_keyboard=True)