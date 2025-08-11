import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch

from CLeVeRMusic import app
from config import YOUTUBE_IMG_URL, OWNER_ID

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
        dev_photo_path = await app.download_media(usr.photo.big_file_id)
        dev_img = Image.open(dev_photo_path).convert("RGB")

        # قص الصورة على شكل مربع
        size = min(dev_img.size)
        left = (dev_img.width - size) // 2
        top = (dev_img.height - size) // 2
        dev_img = dev_img.crop((left, top, left + size, top + size))

        # تكبير الحجم لـ 570×570
        owner_size = 570
        dev_img = dev_img.resize((owner_size, owner_size))

        # إضافة إطار أبيض
        border_size = 10
        border_img = Image.new("RGB", (owner_size + 2*border_size, owner_size + 2*border_size), "white")
        border_img.paste(dev_img, (border_size, border_size))

        # وضع الصورة في الجنب الشمال في النص
        y_pos = (background.height - border_img.height) // 2
        background.paste(border_img, (30, y_pos))

        # ==== كتابة النص "CLeVeR PLAYiNg" بجانب الصورة من الأعلى ====
        draw = ImageDraw.Draw(background)
        font_path = "CLeVeRMusic/assets/font2.ttf"  # خط عريض
        font = ImageFont.truetype(font_path, 60)
        text_x = 30 + border_img.width + 20
        draw.text((text_x, y_pos), "CLeVeR PLAYiNg", fill="white", font=font)

        # ==== باقي البيانات ====
        arial = ImageFont.truetype("CLeVeRMusic/assets/font2.ttf", 30)
        font2 = ImageFont.truetype("CLeVeRMusic/assets/font.ttf", 30)

        draw.text((55, 660), f"{channel} | {views[:23]}", (255, 255, 255), font=arial)
        draw.text((57, 700), clear(title), (255, 255, 255), font=font2)
        draw.line([(55, 760), (1220, 760)], fill="white", width=5, joint="curve")
        draw.ellipse([(918, 748), (942, 772)], outline="white", fill="white", width=15)
        draw.text((36, 785), "00:00", (255, 255, 255), font=arial)
        draw.text((1185, 785), f"{duration[:23]}", (255, 255, 255), font=arial)

        os.remove(f"cache/thumb{videoid}.png")
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"

    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
