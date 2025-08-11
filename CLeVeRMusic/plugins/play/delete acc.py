from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from CLeVeRMusic import app
import config
from pyrogram.errors import FloodWait


                              

@app.on_message(filters.command(["بوت حذف","رابط الحذف","حذف حساب","عاوز احذف"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://telegra.ph/file/7a7e4909d7f78e8d4c685.mp4",
        caption="↢ مع السلامـة تعالى زورنـا كمان مـرة 👋🤍 [اضغط هنا](t.me/LC6Bot)",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

