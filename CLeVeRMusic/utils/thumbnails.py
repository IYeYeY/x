import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch

from CLeVeRMusic import app
from config import YOUTUBE_IMG_URL, OWNER_ID, OWNER_DEVELOPER  # OWNER_ID و OWNER_DEVELOPER من الكونفج

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))

def clear(text):
    words = text.split(" ")
    title = ""
    for i in words:
        if len(title) + len(i) < 60:
            title += " " + i
    return title.strip()

async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            title = re.sub(r"\W+", " ", result.get("title", "Unsupported Title")).title()
            duration = result.get("duration", "Unknown Mins")
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            views = result.get("viewCount", {}).get("short", "Unknown Views")
            channel = result.get("channel", {}).get("name", "Unknown Channel")

        # تحميل صورة الفيديو
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(ImageFilter.BoxBlur(10))
        background = ImageEnhance.Brightness(background).enhance(0.5)

        # ==== جلب صورة الأونر ====
        usr = await app.get_chat(OWNER_ID)

        if usr.photo:
            dev_photo_path = await app.download_media(usr.photo.big_file_id)
        else:
            dev_usr = await app.get_chat(OWNER_DEVELOPER)
            if dev_usr.photo:
                dev_photo_path = await app.download_media(dev_usr.photo.big_file_id)
            else:
                dev_photo_path = None  # مفيش صورة خالص

        if dev_photo_path:
            dev_img = Image.open(dev_photo_path)
            size = min(dev_img.size)
            left = (dev_img.width - size) // 2
            top = (dev_img.height - size) // 2
            dev_img = dev_img.crop((left, top, left + size, top + size))
            owner_size = 570
            dev_img = dev_img.resize((owner_size, owner_size))

            # إضافة إطار أبيض
            border_size = 8
            border_img = Image.new("RGB", (owner_size + 2*border_size, owner_size + 2*border_size), "white")
            border_img.paste(dev_img, (border_size, border_size))

            # موضع صورة الأونر
            img_x = 50
            img_y = (background.height - border_img.height) // 2
            background.paste(border_img, (img_x, img_y))
            text_x = img_x + owner_size + 50
            text_y = img_y
        else:
            # لو مفيش صورة أصلاً
            text_x = 50
            text_y = 50

        draw = ImageDraw.Draw(background)

        # خطوط
        font_big = ImageFont.truetype("CLeVeRMusic/assets/font2.ttf", 70)   # عنوان كبير Bold
        font_small = ImageFont.truetype("CLeVeRMusic/assets/font.ttf", 35)
        arial = ImageFont.truetype("CLeVeRMusic/assets/font2.ttf", 30)
        font = ImageFont.truetype("CLeVeRMusic/assets/font.ttf", 30)

        # العنوان
        draw.text((text_x, text_y), "CLeVeR PLAYiNg", fill="white", font=font_big)

        # اليوزر و ID تحت بعض
        draw.text((text_x, text_y + 90), f"@{usr.username}", fill="#cccccc", font=font_small)
        draw.text((text_x, text_y + 135), f"ID: {usr.id}", fill="#cccccc", font=font_small)

        # باقي المعلومات أسفل
        draw.text((text_x, text_y + 220), clear(title), (255, 255, 255), font=font)
        draw.text((text_x, text_y + 260), f"{channel} | {views[:23]}", (255, 255, 255), font=arial)
        draw.text((text_x, text_y + 300), f"00:00 / {duration}", (255, 255, 255), font=arial)

        os.remove(f"cache/thumb{videoid}.png")
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"

    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
