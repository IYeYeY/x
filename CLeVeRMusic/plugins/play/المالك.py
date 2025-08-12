import asyncio

import os

import time

import requests

from pyrogram import enums

import aiohttp

from pyrogram import filters

from pyrogram import Client

from pyrogram.enums import ChatMemberStatus

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from CLeVeRMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)

from CLeVeRMusic import app

from asyncio import gather

from pyrogram.errors import FloodWait







@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], "")) 

async def ownner(client: Client, message: Message):

    x = []

    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):

         if m.status == ChatMemberStatus.OWNER:

            x.append(m.user.id)

    if len(x) != 0:        

       m = await app.get_users(int(x[0]))

       if m.photo:

         async for photo in app.get_chat_photos(x[0],limit=1):

          await message.reply_photo(photo.file_id,caption=f"𝅄 𓏺 𝐊𝐈𝐍𝐆 :{m.first_name}\n𝅄 𓏺 𝐔𝐒𝐄𝐑 :@{m.username}\n𝅄 𓏺 𝐈𝐃 :{m.id}\n𝅄 𓏺 𝐂𝐇𝐀𝐓: {message.chat.title}\n𝅄 𓏺 𝐈𝐃.𝐂𝐇𝐀𝐓 :{message.chat.id}",reply_markup=InlineKeyboardMarkup(

             [              

               [          

                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")

               ],             

             ]                 

            )                     

          )

       else:

        await message.reply_text(f"𝅄 𓏺 𝐊𝐈𝐍𝐆 :{m.first_name}\n𝅄 𓏺 𝐔𝐒𝐄𝐑 :@{m.username}\n𝅄 𓏺 𝐈𝐃 :{m.id}\n𝅄 𓏺 𝐂𝐇𝐀𝐓: {message.chat.title}\n𝅄 𓏺 𝐈𝐃.𝐂𝐇𝐀𝐓 :{message.chat.id}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))

    else:

        await message.reply_text("الاك محذوف يقلب")

                    

                    
