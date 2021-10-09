from aiogram import types

from loader import dp
from utils.photograph import photo_link
from utils import remove_background


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    new_photo = await remove_background(link)
    await msg.reply_document(document=new_photo, caption='background removed')
    await msg.reply_photo(new_photo, caption='background removed')

