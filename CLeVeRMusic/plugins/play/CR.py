import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from CLeVeRMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)
from CLeVeRMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/WORLE_CLEVER/19",
        caption=f"- 𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐋𝐞𝐕𝐞𝐑 𝐌𝐮𝐬𝐢𝐜 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                   "〘 𝖦𝗋𝖮𝗎𝖯 〙", url=f"https://t.me/T0c_aR"), 
                 InlineKeyboardButton(
                   "〘 𝖲𝗈𝖴𝗋𝖢𝖾 〙",  url=f"https://t.me/xG_Ls"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "〘 𝖧𝖾𝗑 〙", url=f"https://t.me/CL_3Q"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text="𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )


@app.on_message(filters.command(["مطور السورس","بوده","بودا","هكس"], ""), group=73) 
async def deev(client: Client, message: Message):
     user = await client.get_chat(chat_id="CL_3Q")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"هناك شخص بالحاجه اليك عزيزي المطور\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐍𝐚𝐦𝐞 : {name} \n𝐃𝐞𝐯 𝐔𝐬𝐚𝐫 𝐧𝐚𝐦𝐞 : @{username}\n{bio}",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
