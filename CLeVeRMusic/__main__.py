import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from CLeVeRMusic import LOGGER, app, userbot
from CLeVeRMusic.core.call import Zoro
from CLeVeRMusic.misc import sudo
from CLeVeRMusic.plugins import ALL_MODULES
from CLeVeRMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from CLeVeRMusic.plugins.play.azan import azkar

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير مدعوم ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("CLeVeRMusic.plugins" + all_module)
    LOGGER("ميــوزك كليفر").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await Zoro.start()

    await Zoro.decorators()
    LOGGER("ميــوزك كليفر").info("@CL_3Q")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ميــوزك كليفر").info("جارِ ايقاف بوت الميوزك . . .")
    await userbot.start()
    await azkar()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
