import asyncio  
import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from CLeVeRMusic.core.userbot import Userbot
from config import OWNER_ID 
from CLeVeRMusic.utils.database import is_served_chat, add_served_chat, get_served_chats, get_served_users, get_client, set_must, get_must, del_must, get_must_ch, set_must_ch, get_active_chats, remove_active_video_chat, remove_active_chat, set_bot_name, get_bot_name
from CLeVeRMusic import app
import logging
import os

@app.on_message(filters.new_chat_members)
async def handle_new_member(client: Client, message: Message):
    try:
        me = await client.get_me()
        new_members_ids = [user.id for user in message.new_chat_members]
        if me.id not in new_members_ids:
            return

        chat_id = message.chat.id
        title = message.chat.title
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"

        if not await is_served_chat(client, chat_id):
            await add_served_chat(client, chat_id)

        chats = len(await get_served_chats(client))

        try:
            invite_link = await client.export_chat_invite_link(chat_id)
        except Exception:
            invite_link = None

        button = InlineKeyboardButton("〘 رابط الكروب 〙", url=invite_link if invite_link else "https://t.me/")

        await client.send_message(
            OWNER_ID,
            f"<b> ⋡︰تم تفعيل مجموعه تلقائياً\n"
            f"⋡︰عدد المجموعات الان ↫〘 {chats} 〙\n"
            f"⋡︰اسم المجموعه ↫ 〘 {title} 〙\n"
            f"⋡︰بواسطه ↫ 〘 {added_by} 〙 </b>",
            reply_markup=InlineKeyboardMarkup([[button]])
        )

    except Exception as e:
        print(f"حدث خطأ في handle_new_member: {e}")

    message.continue_propagation()
    
    
@app.on_message((filters.group | filters.channel) & filters.text)
async def check_group_activation(client: Client, message: Message):
    try:
        chat_id = message.chat.id
        if not await is_served_chat(client, chat_id):
            await add_served_chat(client, chat_id)

            chats = len(await get_served_chats(client))
            bot_username = (await client.get_me()).username
            mention = message.from_user.mention if message.from_user else message.chat.title

            if message.chat.username:
                group_name = f"[{message.chat.title}](https://t.me/{message.chat.username})"
            else:
                group_name = f"{message.chat.title}"

            await client.send_message(
                OWNER_ID,
                f"<b>≯︰تم تفعيل مجموعه تلقائياً</b>\n"
                f"≯︰عدد المجموعات الان ↫〘 {chats} 〙\n"
                f"≯︰اسم المجموعه ↫ 〘 {group_name} 〙\n"
                f"≯︰بواسطه ↫ 〘 {mention} 〙",
                disable_web_page_preview=True
            )

            await client.send_message(chat_id, "<b>صلي على نبي وتبسم 🤍✨</b>")
    except Exception as e:
        print(f"حدث خطأ في check_group_activation: {e}")

    message.continue_propagation()