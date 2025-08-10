from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from CLeVeRMusic import app
from config import OWNER_ID  # <-- استيراد الآي دي الخاص بالمالك

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel_for_all_except_owner(_, message: Message):
    # التحقق إذا كان مرسل الرسالة هو المالك (المطور)
    if message.from_user.id == OWNER_ID:
        return  # إذا كان هو المطور، لا تفعل شيئًا واخرج من الدالة

    # إذا لم يكن المستخدم هو المطور، سيتم تنفيذ الكود التالي للجميع
    text = "اهلا بك بك عزيزي العضو اليك كيب الاعضاء⚡"
    kep = ReplyKeyboardMarkup(
        [
            ["انميي", "متحركة"],
            ["كتابات", "يـوتيوب"],
            ["لو خيروك"],
            ["اقتباس", "نقشبندي"],
            ["سوال", "اقتباس"],
            ["استوريهات"],
            ["تلاوات", "عبدالباسط"],
            ["صور بنات", "صور ولاد"],
            ["❎ ¦ حذف الكيبورد"],
        ],
        resize_keyboard=True,
    )
    await message.reply(text=text, reply_markup=kep, quote=True)


# باقي الكود يبقى كما هو

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""", reply_markup=ReplyKeyboardRemove()
    )


@app.on_message(filters.regex("يـوتيوب"))
def reply_to_HEY(client: Client, message: Message):
    message.reply_photo(
        photo="https://telegra.ph/file/73299cc44862f1ec277dd.jpg",
        caption="""يتم استخدام هذا الامر لعرض تحميل من اليوتيوب\nاستخدم الامر بهذا الشكل `تنزيل`  او  `يوتيوب`  كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدا """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𝗧𝗲𝗠 𝗝𝗮𝗖𝗞", url="https://t.me/SORCE_CLeVeR" )]]
        ),
    )

