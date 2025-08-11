import asyncio
import datetime
import aiohttp
from pytz import timezone
from pyrogram import Client
from CLeVeRMusic.core.call import Zoro

# مسار ملف الأذان
AZAN_PATH = "CLeVeRMusic/assets/azan.mp3"

# إحداثيات القاهرة
LAT = 30.0444
LON = 31.2357

# تخزين مواقيت الصلاة
prayer_times = {}

async def get_prayer_times():
    global prayer_times
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    url = f"http://api.aladhan.com/v1/timings/{today}?latitude={LAT}&longitude={LON}&method=5"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            timings = data["data"]["timings"]
            prayer_times = {
                "Fajr": timings["Fajr"],
                "Dhuhr": timings["Dhuhr"],
                "Asr": timings["Asr"],
                "Maghrib": timings["Maghrib"],
                "Isha": timings["Isha"]
            }
    print("تم تحديث أوقات الصلاة:", prayer_times)

async def prayer_checker(app: Client):
    cairo_tz = timezone("Africa/Cairo")
    await get_prayer_times()
    while True:
        now = datetime.datetime.now(cairo_tz).strftime("%H:%M")
        for prayer, time_str in prayer_times.items():
            if now == time_str:
                await announce_prayer(app, prayer)
        await asyncio.sleep(30)  # فحص كل 30 ثانية

async def announce_prayer(app: Client, prayer_name: str):
    text = f"حان الآن أذان {prayer_name}"
    async for dialog in app.get_dialogs():
        try:
            await app.send_message(dialog.chat.id, text)
            if dialog.chat.type.name in ["GROUP", "SUPERGROUP"]:
                try:
                    await Zoro.stream_call(AZAN_PATH)
                    await asyncio.sleep(180)  # مدة الأذان 3 دقائق
                    await Zoro.leave_call(dialog.chat.id)
                except Exception as e:
                    print(f"خطأ في تشغيل الأذان في {dialog.chat.id}:", e)
        except Exception as e:
            print(f"خطأ في إرسال الرسالة لـ {dialog.chat.id}:", e)
