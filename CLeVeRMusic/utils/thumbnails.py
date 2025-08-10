import os
import re
import textwrap
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
from config import YOUTUBE_IMG_URL, OWNER_ID
from CLeVeRMusic import app

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def get_thumb(videoid):
    os.makedirs("cache", exist_ok=True)

    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    try:
        results = VideosSearch(videoid, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = re.sub(r"\W+", " ", result.get("title", "Unsupported Title")).title()
            except:
                title = "Unsupported Title"
            duration = result.get("duration", "Unknown Mins")
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            views = result.get("viewCount", {}).get("short", "Unknown Views")
            channel = result.get("channel", {}).get("name", "Unknown Channel")

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(f"cache/thumb_{videoid}.png", mode="wb") as f:
                        await f.write(await resp.read())

        owner = int(OWNER_ID)
        wxyz = await app.download_media(
            (await app.get_users(owner)).photo.big_file_id,
            file_name=f"{owner}.jpg",
        )

        wxy = Image.open(wxyz)
        youtube = Image.open(f"cache/thumb_{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")

        background = image2.filter(ImageFilter.BoxBlur(20))
        background = ImageEnhance.Brightness(background).enhance(0.6)

        Xcenter, Ycenter = wxy.width / 2, wxy.height / 2
        logo = wxy.crop((Xcenter - 250, Ycenter - 250, Xcenter + 250, Ycenter + 250))
        logo.thumbnail((520, 520), Image.Resampling.LANCZOS)
        logo = ImageOps.expand(logo, border=15, fill="white")

        background.paste(logo, (50, 100))

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("CLeVeR/assets/font2.ttf", 40)
        font2 = ImageFont.truetype("CLeVeR/assets/font2.ttf", 70)
        arial = ImageFont.truetype("CLeVeR/assets/font2.ttf", 30)

        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (600, 150), "CLeVeR PLAYING",
            fill="white", stroke_width=2, stroke_fill="white", font=font2
        )
        for line in para:
            if j == 0:
                draw.text((600, 280), line, fill="white", stroke_width=1, stroke_fill="white", font=font)
            elif j == 1:
                draw.text((600, 340), line, fill="white", stroke_width=1, stroke_fill="white", font=font)
            j += 1

        draw.text((600, 450), f"Views : {views[:23]}", (255, 255, 255), font=arial)
        draw.text((600, 500), f"Duration : {duration[:23]} Mins", (255, 255, 255), font=arial)
        draw.text((600, 550), f"Channel : {channel}", (255, 255, 255), font=arial)

        try:
            os.remove(f"cache/thumb_{videoid}.png")
        except:
            pass

        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"

    except Exception as e:
        await app.send_message("z0hary", str(e))
        return YOUTUBE_IMG_URL

