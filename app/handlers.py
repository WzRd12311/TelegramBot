from aiogram import Router
import asyncio
import logging
import random as r
from aiogram import types, F
from config_read import config as c
from app.keyboards import main_menu
from app.inline_keyboards import gallery, quiz, github
from aiogram.filters.command import Command, CommandStart

photo_path = ['https://cdn.discordapp.com/attachments/1236053307013861417/1392553873503158312/image.png?ex=686ff45b&is=686ea2db&hm=56a8560b7eb8ddf7df431fc0e476c28e9ee330b8807c3875168ccd16be454b4e&','https://cdn.discordapp.com/attachments/1236053307013861417/1392553873503158312/image.png?ex=686ff45b&is=686ea2db&hm=56a8560b7eb8ddf7df431fc0e476c28e9ee330b8807c3875168ccd16be454b4e&','https://cdn.discordapp.com/attachments/1236053307013861417/1392553873503158312/image.png?ex=686ff45b&is=686ea2db&hm=56a8560b7eb8ddf7df431fc0e476c28e9ee330b8807c3875168ccd16be454b4e&']

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await asyncio.sleep(1)
    await message.answer("Choose option:", reply_markup=main_menu)


@router.message(F.text == 'Show Photo')
async def cmd_show_photo(message: types.Message):
    await message.answer('Photos:')

    rand_photo = r.choice(photo_path)

    await message.answer_photo(photo=rand_photo)
    await message.answer('Your photo', reply_markup=gallery)


@router.callback_query(F.data == 'more_photo')
async def more_photo(callback: types.CallbackQuery):
    await callback.answer()

    if not photo_path:
        await callback.message.edit_caption(caption='Photos is over.')

    rand_photo = r.choice(photo_path)
   
    new_photo = types.InputMediaPhoto(media=rand_photo, caption=f'One more photo for u!')
    try:
        await callback.message.edit_media(media=new_photo, reply_markup=gallery)
    except:
        pass


@router.callback_query(F.data == 'close_gallery', F.photo)
async def close_gallery(callback: types.CallbackQuery): 
    await callback.answer('Gallery closed.')
    await callback.message.edit_caption(caption="Gallery closed. Choose another options.")


@router.message(F.text == 'Show Quiz')
async def cmd_show_quiz (message: types.Message):
    await message.answer('Quiz will start at soon: ')
    await message.answer('How many times do u use python?', reply_markup=quiz)


@router.callback_query(F.data[0:5] == 'quiz_')
async def quiz_answer(callback: types.CallbackQuery):
    answer_text = ''

    if callback.data == 'quiz_every_day':
        answer_text = 'every day'
    elif callback.data == 'quiz_sometimes':
        answer_text = 'sometimes'
    else:
        answer_text = 'rare'

    await callback.answer(f'Your choice: {answer_text}.')

    await callback.message.edit_text(f'How many times do u use python? Your choice: {answer_text}.', parse_mode='Markdown', reply_markup=None)


@router.message(F.text == 'Show Git Hub')
async def cmd_my_github (message: types.Message):
    
    await message.answer(f'My github:', reply_markup=github)

@router.message(F.content_type.in_([types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.STICKER, types.ContentType.TEXT]))
async def cmd_answer(message: types.Message):
    if message.photo:
        await message.reply_photo(photo=message.photo[-1].file_id, caption="THX for photo!")
    elif message.video:
        await message.reply_video(video=message.video.file_id, caption="THX for video!")
    elif message.sticker:
        await message.reply_sticker(sticker=message.sticker.file_id, caption="THX for sticker!")
        await message.reply('THX for sticker')
    else:
        await message.reply(f"THX for {message.content_type}!")