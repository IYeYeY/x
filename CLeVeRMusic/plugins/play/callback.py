import time
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
from CLeVeRMusic.plugins.play.start import devs
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
from config import OWNER, GROUP, YOUTUBE_IMG_URL, OWNER_DEVELOPER, OWNER_NAME, PHOTO, VIDEO




@app.on_callback_query(filters.regex("arbic") & ~BANNED_USERS)
async def arbic(client: Client, query: CallbackQuery):
    bot = await client.get_me()
    BOT_NAME = await get_bot_name(bot.username)
    ch = await get_must(bot.username) or "None"
    dev = config.OWNER_ID
    await query.answer("القائمة الرئيسية")
    await query.edit_message_text(
        f"<b>اهلا بك في بوت ↫  {BOT_NAME} \n\n</b>"
        f"<b>بوت خاص لتشغيل الأغاني الصوتية والمرئية.\n</b>"
        f"<b>قم بإضافة البوت إلى مجموعتك أو قناتك.\n</b>"
        f"<b>سيتم تفعيل البوت وانضمام المساعد.\n</b>"
        f"<b>استخدم الأزرار لمعرفة أوامر الاستخدام.</b>",
        reply_markup=InlineKeyboardMarkup(
            [
               [InlineKeyboardButton(text="❲ لتنصيب بوت مماثل ❳", url=f"https://t.me/{OWNER[0]}")],
                [
                    InlineKeyboardButton("❲ اوامر التشغيل ❳", callback_data="bcmds"),
                    InlineKeyboardButton("❲ اوامر التفعيل ❳", callback_data="bhowtouse"),
                ],
                [
                    InlineKeyboardButton(text="❲ المطور ❳", user_id=dev),
                    InlineKeyboardButton(text="❲ قناة البوت ❳", url=f"{ch}"),
                ],
                [
                    InlineKeyboardButton(text="❲ 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌 ❳", url=f"https://t.me/{bot.username}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_callback_query(filters.regex("english") & ~BANNED_USERS)
async def english(client: Client, query: CallbackQuery):
    bot = await client.get_me()
    BOT_NAME = await get_bot_name(bot.username)
    ch = await get_must(bot.username) or "None"
    dev = config.OWNER_ID
    await query.answer("Home Start")
    await query.edit_message_text(
        f"""<b>≯︰Hello ↫ ❲ {query.from_user.mention} ❳ \n\n≯︰I am a bot to play songs in calls\n≯︰I can play in a group or channel\n≯︰Just add me and raise me as a moderator </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="❲ لتنصيب بوت مماثل ❳", url=f"https://t.me/{OWNER[0]}")],
                [
                    InlineKeyboardButton("❲ Operating commands  ❳", callback_data="bcmds"),
                    InlineKeyboardButton("❲ Activation commands  ❳", callback_data="bhowtouse"),
                ],
                [
                    InlineKeyboardButton(text="❲ Developer  ❳", user_id=dev),
                    InlineKeyboardButton(text="❲ Developer Channel  ❳", url=f"{ch}"),
                ],
                [
                    InlineKeyboardButton(text="❲ 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌 ❳", url=f"https://t.me/{bot.username}?startgroup=true"),
                ],
            ]
        )
    )


@app.on_callback_query(filters.regex("cbcmds") & ~BANNED_USERS)
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f""" <b>هلو [{query.message.from_user.first_name}](tg://user?id={query.message.from_user.id}) !</b>
❲ : </b>تيست ٢""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Bisc Cmd", callback_data="cbbasic"),
                ],[
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo")
                ],[
                    InlineKeyboardButton("Go Back ", callback_data="english")
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""<b>≯︰طريقه تفعيل البوت ↯.<b>

<b>≯︰اضف البوت الى المجموعه او القناة</b>
<b>≯︰ارفع البوت ادمن مع كل الصلاحيات</b>
<b>≯︰ابدأ مكالمه جماعيه جديده</b>
<b>≯︰ارسل تشغيل مع اسم المقطع المطلوب</b>
<b>≯︰سينظم المساعد تلقائيا ويبدا التشغيل</b>
<b>≯︰في حال واجهت اي مشكلة اخرى يمكنك التواصل مع المطور </b>
<b>⚡  Developer by """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="english")]]
        ),
    )

@app.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
         f"""≯︰اوامر التشغيل في المجموعه او القناة ↯.

≯︰ تشغيل ↫ لتشغيل الموسيقى  
≯︰فيديو  ↫ لتشغيل مقطع فيديو 
≯︰تشغيل عشوائي  ↫ لتشغيل اغنيه عشوائيه 
≯︰ابحث ↫ للبحث في اليوتيوب
≯︰يوت او تنزيل او نزل + اسم الاغنيه ↫ لتحميل Mp3
≯︰حمل + اسم الفيديو ↫ لتحميل فيديو</b>
<b>≯︰في حال واجهت اي مشكلة اخرى يمكنك التواصل مع المطور </b>
<b>Developer by ⚡ """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@app.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
                f"""≯︰اوامر الادمنيه ↯. 

<b>≯︰استئناف - لتكمله التشغيل</b>
<b>≯︰تخطي ↫ لتخطي المقطع المشغل</b>
<b>≯︰ايقاف مؤقت - ايقاف التشغيل موقتأ</b>
<b>≯︰ايقاف ≯︰انهاء ↫ لانهاء تشغيل المقطع </b>
<b>≯︰تكرار ≯︰كررها ↫ لتكرار تشغيل المقطع</b>
<b>≯︰في حال واجهت اي مشكلة اخرى يمكنك التواصل مع المطور</b>
<b>⚡  Developer by </b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@app.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("SUDO COMMANDS")
    await query.edit_message_text(
        f"""≯︰اوامر مطورين البوت ↯.
<b>≯︰الاحصائيات </b>
<b>≯︰الكروبات</b>
<b>≯︰المشتركين</b>
<b>≯︰تعيين اسم البوت </b>
<b>≯︰اوامر الاذاعه</b>
<b>≯︰تغيير مكان الاشعارات </b>*
<b>≯︰تفعيل ≯︰تعطيل الاشعارات</b>
<b>≯︰اعدادات الحساب المساعد</b>
<b>≯︰في حال واجهت اي مشكلة اخرى يمكنك التواصل مع المطور </b>
<b>Developer by ⚡ """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❲ للخلف ❳", callback_data="cbcmds")]]
        ),
    )


@app.on_callback_query(filters.regex("bhowtouse"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""</b>≯︰طريقه تفعيل البوت ↯.<b>

</b>≯︰اضف البوت الى المجموعه او القناة</b>
<b>≯︰ارفع البوت ادمن مع كل الصلاحيات</b>
<b>≯︰ابدأ مكالمه جماعيه جديده</b>
<b>≯︰ارسل تشغيل مع اسم المقطع المطلوب</b>
<b>≯︰سينظم المساعد تلقائيا ويبدا التشغيل</b>
<b>≯︰في حال لم ينضم المساعد راسل الدعم من  هنا  </b>
<b>Developer by ⚡ """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❲ للخلف ❳", callback_data="arbic")]]
        ),
    )


@app.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>≯︰اهلا بك في بوت ↫❲ <a href='tg://user?id={query.from_user.id}'>{query.from_user.first_name}</a> ❳  
≯︰اختر ما تريده من اوامر البوت ↯</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❲ اوامر التشغيل ❳", callback_data="bbasic"),
                    InlineKeyboardButton("❲ اوامر الادمنيه ❳", callback_data="badmin"),
                ],
                [
                    InlineKeyboardButton("❲ اوامر المطورين ❳", callback_data="bsudo"),
                    InlineKeyboardButton("❲ اوامر الحمايه ❳", callback_data="acbsecurity"),
                ],
                [
                    InlineKeyboardButton("❲ اوامر اضافية ❳", callback_data="youj")
                ],
                [
                    InlineKeyboardButton("❲ القائمه الاساسيه ❳", callback_data="arbic")
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>≯︰اوامر التشغيل في المجموعه او القناة ↯.

≯︰تشغيل ↫ لتشغيل الموسيقى  
≯︰فيديو  ↫ لتشغيل مقطع فيديو 
≯︰تشغيل عشوائي  ↫ لتشغيل اغنيه عشوائيه 
≯︰ابحث ↫ للبحث في اليوتيوب
≯︰يوت او تنزيل او نزل + اسم الاغنيه ↫ لتحميل Mp3
≯︰حمل + اسم الفيديو ↫ لتحميل فيديو"
≯︰في حال واجهت اي مشكلة اخرى يمكنك التواصل مع المطور
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❲ للخلف ❳", callback_data="bcmds")]]
        ),
    )


@app.on_callback_query(filters.regex("badmin"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>≯︰اوامر الادمنيه ↯. 

≯︰استئناف - لتكمله التشغيل
≯︰تخطي ↫ لتخطي المقطع المشغل
≯︰ايقاف مؤقت - ايقاف التشغيل موقتأ
≯︰ايقاف ≯︰انهاء ↫ لانهاء تشغيل المقطع 
≯︰تكرار ≯︰كررها ↫ لتكرار تشغيل المقطع
≯︰في حال واجهت اي مشكلة اخرى يمكنك التواصل مع المطور
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❲ للخلف ❳", callback_data="bcmds")]]
        ),
    )

@app.on_callback_query(filters.regex("bsudo"))
async def sudo_set(client: Client, query: CallbackQuery):
    await query.answer(" اوامر المطورين")
    await query.edit_message_text(
       f"""<b>≯︰اوامر مطورين البوت ↯.
≯︰بنك
≯︰الاحصائيات 
≯︰الكروبات
≯︰المشتركين
≯︰تعيين اسم البوت 
≯︰اوامر الاذاعه
≯︰تغيير مكان الاشعارات 
≯︰تفعيل ≯︰تعطيل الاشعارات
≯︰اعدادات الحساب المساعد
≯︰في حال واجهت اي مشكلة اخرى يمكنك التواصل مع المطور""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❲ للخلف ❳", callback_data="bcmds")]]
        ),
    )
@app.on_callback_query(filters.regex("acbsecurity"))
async def acbsecurity(_, query: CallbackQuery):
    await query.answer(
        "≯︰اوامر الحماية غير متاحة حاليا. 🚧",
        show_alert=True
    )
    
    
@app.on_callback_query(filters.regex("youj"))
async def youj(_, query: CallbackQuery):
    await query.answer(
        "اوامر الإضافية غير متاحة حاليا. 🚧",
        show_alert=True
    )    
    
@app.on_callback_query(filters.regex("jhg"))
async def jhg(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>الاوامر الإضافية ⚡:
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
≯︰صراحه » اسئلة صراحه
≯︰الجاسوس » لعبة ترفيهيه 
≯︰تويت » اسئله ترفيهيه
≯︰اعلام » معرفة الاعلام من الصور
≯︰لغز » الغاز مشهوره
≯︰مشاهير » معرفة المشاهير من الصور
≯︰ممثلين » معرفه الممثلين من الصور
≯︰مغنين » معرفه المغنين من الصور
≯︰لاعبين » معرفه اللاعبين من الصور
≯︰لو خيروك » اختار حاجه من اتنين
≯︰تحدي » تحديات مسليه 
≯︰مختلف » معرفه الرمز المختلف
≯︰امثله » امثله معروفه 
≯︰تفكيك » تركب الكلمه المفككه
≯︰فزوره » فزوره مشوره وتحلها
≯︰اسئله » اسئله متنوعه
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❲ للخلف ❳", callback_data="bcmds")]]
        ),
    )    
    

