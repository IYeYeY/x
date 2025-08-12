import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from CLeVeRMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)
from CLeVeRMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(filters.command(["المطور"], ""))
async def khfzss(client: Client, message: Message):
    usrr = await client.get_chat(OWNER_ID)
    name = usrr.first_name
    bio = usrr.bio
    id = usrr.id
    username = usrr.username
    async for photo in client.get_chat_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""𝅄 𓏺 DeVeLoPer BoT Music .\n\n𝅄 𓏺 UsEr : @{username} \n𝅄 𓏺 Id : {id} \n𝅄 𓏺 BiO : {bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{username}")
                ],
            ]
        ),
    )                    
                

                    chat = message.chat.id
    gti = message.chat.title
    chatusername = f"@{message.chat.username}"
    link = await app.export_chat_invite_link(chat)
    user = await client.get_users(message.from_user.id)
    user_id = message.from_user.id
    user_ab = message.from_user.username
    user_name = message.from_user.first_name
    buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await app.send_message(OWNER_ID, f"<b>𝅄 𓏺 قام {message.from_user.mention}\n</b>"
                                     f"<b>𝅄 𓏺 بمناداتك عزيزي المطور\n</b>"
                                     f"<b>𝅄 𓏺 الأيدي {user_id}\n</b>"
                                     f"<b>𝅄 𓏺 اليوزر @{user_ab}\n</b>"
                                     f"<b>𝅄 𓏺 ايدي المجموعة {message.chat.id}\n</b>"
                                     f"<b>𝅄 𓏺 يوزر المجموعه {chatusername}</b>",
                                     reply_markup=reply_markup)

@app.on_message(filters.command(["تحويل لصوره"], ""))
async def elkatifh(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



