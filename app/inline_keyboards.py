from aiogram.types import InlineKeyboardMarkup as IKM
from aiogram.types import InlineKeyboardButton as IKB

gallery = IKM(inline_keyboard=[
	[
	IKB(text='More Photo', callback_data='more_photo'),
	IKB(text='Close Gallery', callback_data='close_gallery')
	]
	])


quiz = IKM(inline_keyboard=[
	[
	IKB(text='Every day', callback_data='quiz_every_day'), 
	IKB(text='Sometimes', callback_data='quiz_sometimes'), 
	IKB(text='Rare', callback_data='quiz_rare')
	]
	])


github = IKM(inline_keyboard=[[IKB(text='Go to GitHub', url='https://github.com/WzRd12311', callback_data='git')]])