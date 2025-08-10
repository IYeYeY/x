from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant, ChatAdminRequired
from pyrogram.types import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb
from CLeVeRMusic import app
from CLeVeRMusic.utils.database import get_must, get_must_ch

def must_join_ch(zohary):
    async def ch_user(c, msg):
        try:
            if not msg.from_user:
                return await zohary(c, msg)

            is_must_enabled = await get_must_ch(app.username)
            if is_must_enabled != "مفعل":
                return await zohary(c, msg)

            channel_url = await get_must(app.username)
            if not channel_url:
                return await zohary(c, msg)

            channel_username = channel_url.replace("https://t.me/", "")

            try:
                member_status = await app.get_chat_member(channel_username, msg.from_user.id)
                if member_status.status in [
                    ChatMemberStatus.MEMBER,
                    ChatMemberStatus.ADMINISTRATOR,
                    ChatMemberStatus.OWNER,
                ]:
                    return await zohary(c, msg)
                else:
                    raise UserNotParticipant
            except UserNotParticipant:
                await msg.reply(
                    f"<b> 🚦 يجب ان تشترك في القناة\n\nقنـاة الـبـوت : « {channel_url} »</b>.",
                    disable_web_page_preview=True,
                    reply_markup=ikm([
                        [ikb("❲ اضغط للاشتراك بالقناة ❳", url=channel_url)]
                    ])
                )
                return
            except ChatAdminRequired:
                return await zohary(c, msg)

        except Exception as e:
            print(f"حدث خطأ أثناء التحقق من الاشتراك: {e}")
            return await zohary(c, msg)

        return await zohary(c, msg)

    return ch_user