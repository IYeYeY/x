from pyrogram import Client, filters
from colorama import init, Style
from pyrogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb 
from CLeVeRMusic import app
from config import OWNER_ID, OWNER_DEVELOPER
from CLeVeRMusic.utils.database import get_served_chats, is_contact_enabled, toggle_contact, is_served_user, add_served_user, get_served_users, get_client, set_must, get_must, del_must, get_must_ch, set_must_ch, get_active_chats, remove_active_video_chat, remove_active_chat, set_bot_name, get_bot_name
import os 
from pyrogram.enums import ParseMode
import shutil
import asyncio
import random 
from asyncio import gather
import time
import logging
from PIL import Image
from pyrogram import client, filters
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
from CLeVeRMusic.utils.database import get_must, get_bot_name
import config
from CLeVeRMusic import app
from CLeVeRMusic.misc import _boot_
from CLeVeRMusic.utils.database import (
    add_served_chat,
    is_served_channel,
    is_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    get_served_chats, 
    get_served_users, 
    is_banned_user,
    is_on_off,
)
from CLeVeRMusic.plugins.tools.must_join import must_join_ch
from CLeVeRMusic.utils.formatters import get_readable_time
from config import BANNED_USERS
from strings import get_string
import logging
import os
import re
import textwrap
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch
from CLeVeRMusic import app
from pathlib import Path 
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps
import aiofiles
import aiohttp
from pyrogram.types import CallbackQuery
from config import OWNER, GROUP, YOUTUBE_IMG_URL, OWNER__ID, OWNER_DEVELOPER, OWNER_NAME, PHOTO, VIDEO

async def gen_bot(client, username, photo):
    photo_path = Path("./photo")
    photo_path.mkdir(parents=True, exist_ok=True)
    output_file = photo_path / f"{username}.png"
    if output_file.is_file():
        return str(output_file)
    photo_path = await client.download_media(photo)
    background = Image.open(photo_path)
    background.save(output_file)
    return str(output_file)
    
devs = filters.user([OWNER__ID,OWNER_DEVELOPER,OWNER_ID])

@app.on_message(filters.command(["/start", "❲ رجوع للقائمة الرئيسية ❳"], ""))
@must_join_ch
async def start_pm(client, message: Message):
    try:
        user_id = message.from_user.id
        bot = await client.get_me()
        BOT_NAME = await get_bot_name(bot.username)
        ch = await get_must(bot.username) or "None"
        dev = config.OWNER_ID
        if user_id in [OWNER__ID, OWNER_DEVELOPER, OWNER_ID]:
            keyboard = ReplyKeyboardMarkup(
                [
                    ["❲ تعيين اسم البوت ❳"],
                    ["❲ تفعيل التواصل ❳", "❲ تعطيل التواصل ❳"],
                    ["❲ المكالمات النشطه ❳"],
                    ["❲ قسم الاحصائيات ❳", "❲ قسم المساعد ❳"],
                    ["❲ قسم الاشتراك الاجباري ❳", "❲ قسم الاذاعه ❳"],
                    ["❲ تنظيف التحميلات ❳", "❲ مطورين السورس ❳"],
                    ["❲ حذف الكيبورد ❳"]
                ], resize_keyboard=True
            )
            return await message.reply("<b> ≭︰اهلا بك حبيبي المطور  </b>", reply_markup=keyboard)

        await add_served_user(client, user_id)

        sddd = (
            f"<b>≯︰اهلا بك في بوت ↫  {BOT_NAME} \n\n</b>"
            f"<b>≯︰بوت خاص لتشغيل الأغاني الصوتية والمرئية\n</b>"
            f"<b>≯︰قم بإضافة البوت إلى مجموعتك أو قناتك\n</b>"
            f"<b>≯︰سيتم تفعيل البوت وانضمام المساعد\n</b>"
            f"<b>≯︰استخدم الأزرار لمعرفة أوامر الاستخدام</b>"
        )

        buttons = [
                [InlineKeyboardButton(text="❲ لتنصيب بوت مماثل ❳", url=f"https://t.me/{OWNER[0]}")],
                [
                    InlineKeyboardButton("❲ اوامر التشغيل ❳", callback_data="bcmds"),
                    InlineKeyboardButton("❲ اوامر التفعيل ❳", callback_data="bhowtouse"),
                ],
                [
                    InlineKeyboardButton("❲ المطور ❳", user_id=dev),
                    InlineKeyboardButton("❲ قناة البوت ❳", url=f"{ch}"),
                ],
                [
                    InlineKeyboardButton("❲ 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌 ❳", url=f"https://t.me/{bot.username}?startgroup=true"),
                ],
            ]

        if not bot.photo:
            await client.send_message(
                message.chat.id,
                sddd,
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        else:
            photo = bot.photo.big_file_id
            image_path = await gen_bot(client, bot.username, photo)
            await client.send_photo(
                message.chat.id,
                photo=image_path,
                caption=sddd,
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    except Exception as e:
        print(f"خطأ في أمر /start: {e}")

@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    try:
        bot = await client.get_me()
        BOT_NAME = await get_bot_name(bot.username)
        ch = await get_must(bot.username) or "None"
        dev = config.OWNER_ID
        chat_id = message.chat.id

        if message.new_chat_members[0].id == bot.id:
            # الحصول على صورة البوت من get_me()
            photo = bot.photo.big_file_id if bot.photo else None
            image_path = await gen_bot(client, bot.username, photo) if photo else None

            buttons = [
                [InlineKeyboardButton(text="❲ لتنصيب بوت مماثل ❳", url=f"https://t.me/{OWNER[0]}")],
                [
                    InlineKeyboardButton("❲ اوامر التشغيل ❳", callback_data="bcmds"),
                    InlineKeyboardButton("❲ اوامر التفعيل ❳", callback_data="bhowtouse"),
                ],
                [
                    InlineKeyboardButton("❲ المطور ❳", user_id=dev),
                    InlineKeyboardButton("❲ قناة البوت ❳", url=f"{ch}"),
                ],
                [
                    InlineKeyboardButton("❲ 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌 ❳", url=f"https://t.me/{bot.username}?startgroup=true"),
                ],
            ]

            await message.reply_photo(
                photo=image_path if image_path else None,
                caption="<b>≯︰اهلا بك في بوت تشغيل الاغاني \n≯︰تم تفعيل البوت في المجموعه تلقائيا \n≯︰يمكنك تشغيل الموسيقى الان 🎶</b>",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

            await add_served_chat(client, chat_id)

    except Exception as e:
        print(f"حدث خطأ أثناء الترحيب: {e}")
        
@app.on_message(filters.command(["❲ تفعيل التواصل ❳"],"") & filters.private & devs, group = 3948)
async def enable_contact(client: Client, message: Message):
    await toggle_contact(client, enable=True)
    await message.reply_text("<b>≯︰تم تفعيل التواصل.</b>.")

@app.on_message(filters.command(["❲ تعطيل التواصل ❳"],"") & filters.private & devs, group = 249494)
async def disable_contact(client: Client, message: Message):
    await toggle_contact(client, enable=False)
    await message.reply_text("<b>≯︰تم تعطيل التواصل.</b>")

@app.on_message(filters.private & ~filters.user(OWNER_ID))
async def forward_messages_to_owner(client: Client, message: Message):
    if await is_contact_enabled(client):  # تحقق من حالة التواصل قبل تحويل الرسالة
        await message.forward(OWNER_ID)
        message.continue_propagation()
    else:
        message.continue_propagation()  # إذا كان التواصل معطل، فقط استمر في المعالجة دون تحويل
    
@app.on_message(filters.command(["❲ حذف الكيبورد ❳"],"") & filters.private & devs, group = 2)
async def delete_keyboard(c,msg):
    await msg.reply("<b> ≭︰تم ازالة الكيبورد عزيزي المطور </b>", reply_markup = ReplyKeyboardRemove())



bot = [
    "<b>عوفني بحالي</b>",
    "<b>نعم يگلب گلبي</b>",
    "<b>گول شرايد</b>",
    "<b>تحجي شرايد ؟ لو اكتمك 🌚</b>",
    "<b>گول يقلبو</b>",
    "<b>عيون {} العسليات</b>",
     "<b>عيون {} </b>",
    "<b>نعم يقلب {}</b>",
    "<b>شبيك ولك ؟ صار ساعه تصيح</b>",
    "<b>دكوم بيه</b>",
    "<b>قلب {}</b>",
    "<b>نجب</b>",
    "<b>بذمتك اذا انت بدالي تقبل يسوون بيك هيج ؟</b>",
]

selections = [
    "<b>اسمي {} ولك</b>",
    "<b>كافي كتلك اسمي {}</b>",
    "<b>انت البوت امشي ولي 😂</b>",
    "<b>گول</b>",
    "<b>راسي صار يوجعني من وراك امشي ولي</b>",
    "<b>يعم والله بحبك بس ناديلي {}</b>",
    "<b>تدري راح احبك اكتر لو ناديتلي {}</b>",
    "<b>اسكت كافي دوختني</b>",
    "<b>ما فارغ لك ولي</b>",
    "<b>ولك احجي شرايد</b>",
    "<b>ورحمه ابويا اسمي {}</b>",
]

@app.on_message(filters.command("❲ تعيين اسم البوت ❳", ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id,"<b> ≭︰ ارسل اسم البوت الجديد الان </b>", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("<b> ≭︰ تم تعين اسم البوت بنجاح </b>")



@app.on_message(filters.command(["بوت", "البوت"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"<a href=https://t.me/{bot_username}?startgroup=True>  {bar} </a>", disable_web_page_preview=True)

@app.on_message(filters.text)
async def bott(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    if message.text == BOT_NAME:
      bar = random.choice(bot).format(BOT_NAME)
      await message.reply_text(f"<a href=https://t.me/{bot_username}?startgroup=True> {bar} </a>", disable_web_page_preview=True)
    message.continue_propagation()


@app.on_message(filters.command(["❲ مطورين السورس ❳"], "") & filters.private, group=2)
async def devs_source(client, message):
    kep = ReplyKeyboardMarkup(
        keyboard=[
            ["❲ المطور الاول ❳", "❲ المطور الثاني ❳"],
            ["❲ رجوع للقائمة الرئيسية ❳"]
        ],
        resize_keyboard=True
    )
    await message.reply(
        "<b>≯︰اهلا بك عزيزي المطور لرؤية معلومات المطورين قم بالضغط على الأزرار بالأسفل</b>",
        reply_markup=kep
    )


@app.on_message(filters.command(["❲ المطور الاول ❳", "❲ المطور الثاني ❳"], "") & filters.private, group=2)
async def dev_source(client, message):
    if message.text == "❲ المطور الاول ❳":
        user_id = OWNER_DEVELOPER  
    else:
        user_id = OWNER__ID  

    user = await client.get_users(user_id)
    text = f"<b>• 𝖭𝖺𝗆𝖾 : {user.mention}</b>\n<b>• 𝗂𝖣 : {user.id}</b>"
    
    chat = await client.get_chat(user.id)
    if chat.bio:
        text += f"\n<b>• 𝖡𝗂𝗈 : {chat.bio}</b>"
    
    if user.photo:
        async for photo in client.get_chat_photos(user.id, limit=1):
            await message.reply_photo(photo.file_id, caption=text)
    else:
        await message.reply(text)


@app.on_message(filters.command(["غادر", "غادري"], "") & filters.group)
async def leave_group(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id  
    dev = await OWNER_ID
    if user_id not in [dev, OWNER_DEVELOPER]:
        return await message.reply_text("<b>≯︰فقط المطور الأساسي يمكنه استخدام الأمر.</b>")

    if message.chat.type == enums.ChatType.GROUP or message.chat.type == enums.ChatType.SUPERGROUP:
        chat_title = message.chat.title
        await message.reply_text(f"<b>≯︰يغادر البوت {chat_title} الآن...</b>")
        return await client.leave_chat(message.chat.id)




@app.on_message(filters.command(["❲ ترويج للبوت ❳"],"") & filters.private & devs, group = 2)
async def broadcast_bot_(c: Client ,msg):
    try:
        owner = await c.get_users(int(OWNER_ID))
        chats = await get_served_chats(c) 
        x = 0
        for chat in chats:
            try:
                await c.send_message(int(chat["chat_id"]),f"<b> ≭︰ بوت ميوزك قنوات كروبات   ، البوت يعمل بسرعة وجودة خارقة ، بدون تهنيج ولا تقطيع لان البوت شغال علي سيرفر لوحدو◟</b>\n\n<b>• ارفع البوت فـ قناتك او كروبك وجرب سرعة البوت بنفسك وشوف المميزات◟</b>\n\n<b>• يوزر البوت : @{c.me.username} ◟ </b>\n<b>• يوزر المطور : @{owner.username if owner.username else owner.mention} ◟</b>", reply_markup=ikm([[ikb("𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .", url=f"https://t.me/{app.username}?startgroup=true")]]))
                x += 1
                await asyncio.sleep(0.2)
            except Exception as e:
                pass
        await msg.reply(f"<b> ≭︰تم ارسال الى {x} كروب </b>")
        users = await get_served_users(c) 
        x = 0
        for chat in users:
            try:
                await c.send_message(int(chat["user_id"]),f"<b> ≭︰ بوت ميوزك قنوات كروبات    ، البوت يعمل بسرعة وجودة خارقة ، بدون تهنيج ولا تقطيع لان البوت شغال علي سيرفر لوحدو◟</b>\n\n<b>• ارفع البوت فـ قناتك او كروبك وجرب سرعة البوت بنفسك وشوف المميزات◟</b>\n\n<b>• يوزر البوت : @{c.me.username} ◟ </b>\n<b>• يوزر المطور : @{owner.username if owner.username else owner.mention} ◟</b>", reply_markup=ikm([[ikb("𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .", url=f"https://t.me/{app.username}?startgroup=true")]]))
                x += 1
                await asyncio.sleep(0.2)
            except Exception as e:
                pass
        await msg.reply(f"<b> ≭︰تم ارسال الى {x} مستخدم </b>")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")
        
        
        
