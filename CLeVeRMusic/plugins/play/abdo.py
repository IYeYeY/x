from pyrogram import Client, filters, enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPrivileges
from CLeVeRMusic import app

welcome_enabled = True

@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        chat_id = chat_member_updated.chat.id

        if kicked_by is None:
            message = f"⋡ المستخدم [{user.first_name}](tg://user?id={user.id}) تم طرده."
        elif kicked_by.is_self:
            message = f"⋡ المستخدم [{user.first_name}](tg://user?id={user.id}) تم طرده بواسطة البوت."
        else:
            try:
                await client.ban_chat_member(chat_id, kicked_by.id)
                message = (
                    f"⋡ المستخدم [{user.first_name}](tg://user?id={user.id}) تم طرده بواسطة ⋡"
                    f"[{kicked_by.first_name}](tg://user?id={kicked_by.id})\n تم حظر الشخص الذي طرد العضو ⋡"
                )
            except Exception:
                message = (
                    f"⋡ المستخدم [{user.first_name}](tg://user?id={user.id}) تم طرده بواسطة "
                    f"[{kicked_by.first_name}](tg://user?id={kicked_by.id})\n⋡ لم أستطع حظر المشرف."
                )

        await client.send_message(chat_id, message)


@app.on_message(filters.command("رفع مشرف", "") & filters.group)
async def promote_g_admin(client, message):
    sender_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if sender_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await message.reply("يجب أن تكون مشرف أو مالك لاستخدام هذا الأمر ⋡")
        return

    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
    else:
        await message.reply("الرجاء الرد على رسالة المستخدم لرفع مشرف ⋡")
        return

    privileges = ChatPrivileges(
        can_manage_chat=True,
        can_delete_messages=True,
        can_manage_video_chats=True,
        can_restrict_members=True,
        can_promote_members=True,
        can_change_info=True,
        can_post_messages=False,
        can_edit_messages=False,
        can_invite_users=True,
        can_pin_messages=True,
    )

    try:
        await client.promote_chat_member(message.chat.id, user_id, privileges=privileges)
        await message.reply(f"تم رفع [{user_id}](tg://user?id={user_id}) مشرف بنجاح ⋡")
    except Exception as e:
        await message.reply(f"⋡ فشل رفع المشرف: {e}")
