#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image
import os
from pyzbar.pyzbar import decode
from bot.plugins.display.display_progress import progress
from env import EnvData 
from messages import Message

@Client.on_message(filters.photo)
async def qr_decode(client, message):
    if EnvData.UPDATE_CHANNEL:
        try:
            user = await bot.get_chat_member(EnvData.UPDATE_CHANNEL, message.chat.id)
            if user.status == "kicked":
              await client.send_message(text=Message.BANNED_USER_TEXT)
              return
        except UserNotParticipant:
            await client.send_message(chat_id=message.chat.id, text=Message.FORCE_SUBSCRIBE_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="😎 Join Channel 😎", url=f"https://telegram.me/{EnvData.UPDATE_CHANNEL}")]]))
            return
        except Exception:
            await client.send_message(chat_id=message.chat.id, text=Message.SOMETHING_WRONG)
            return
    decode_text = await client.send_message(
        chat_id=message.chat.id,
        text="<b>Processing your request...</b>",
        reply_to_message_id=message.message_id,
    )
    dl_location = str(message.from_user.id)
    im_dowload = ''
    qr_text = ''
    try:
        im_dowload = await message.download(
            file_name=dl_location + '.png',
            progress=progress,
            progress_args=(
                "Trying to download....",
                decode_text
            )
        )
    except Exception as error:
        print(error)
    await decode_text.edit(
        text="Decoding....."
    )
    try:
        qr_text_data = decode(Image.open(im_dowload))
        qr_text_list = list(qr_text_data[0])  # Listing
        qr_text_ext = str(qr_text_list[0]).split("'")[1]  # Text Extract
        qr_text = "".join(qr_text_ext)  # Text_join
    except Exception as error:
        print(error)
    await decode_text.edit_text(
        text=f"<b>Link :-</b> <code>{qr_text}</code>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Open Link", url=f"{qr_text}"), InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={qr_text}"), ],
                                           [InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')]]),
        disable_web_page_preview=True
    )
    try:
        os.remove(im_dowload)
    except Exception as error:
        print(error)
