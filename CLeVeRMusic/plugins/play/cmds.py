import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from CLeVeRMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["〘 الاوامر 〙   ","الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://t.me/WORLE_CLEVER/26",
        caption=f"⋠ 𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐋𝐞𝐕𝐞𝐑 𝐌𝐮𝐬𝐢𝐜 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〘 اوامر التشغيل 〙", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "〘 اوامر القناة 〙", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "〘 اوامر الادمن 〙", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "〘 اوامر المطور 〙", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "〘 𝖲𝗈𝖴𝗋𝖢𝖾 𝖢𝖫𝖾𝖵𝖾𝖱 〙", url="https://t.me/xG_Ls"),
                ],
            ]
        ),
    )


