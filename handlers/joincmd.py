# A Plugin From Daisyxmusic (Telegram bot project)
# Copyright (C) 2021  Inukaasith

from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["joingrp"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>tf? ᴏɴᴄᴇ ʙᴇɴɪ ɢʀᴜʙᴜɴ ʏᴏɴᴇᴛɪᴄɪꜱɪ ᴏʟᴀʀᴀᴋ ᴇᴋʟᴇ! ᴀʀᴅɪɴᴅᴀɴ ʙᴜ ᴋᴏᴍᴜᴛᴜ ᴋᴜʟʟᴀɴɪɴ!</b> 😄",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "JackMusicAssistant" # F this

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"ᴛᴀᴍᴀᴍ! ɪꜱᴛᴇᴅɪɢɪɴ ɢɪʙɪ ʙᴜʀᴀʏᴀ ᴋᴀᴛɪʟᴅɪᴍ! ꜱᴘᴀᴍ ʏᴀᴘᴍᴀʏɪɴ ʏᴏᴋꜱᴀ ꜱɪᴢɪ ʙᴀɴ ᴇᴅᴇʀɪᴍ! 😂")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>ʏᴀʏɪɴᴄɪ ʜᴇꜱᴀʙɪ ᴢᴀᴛᴇɴ ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇ!</b> ɢɪʙɪ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀʏɪɴ. <b>kid</b> 😒",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"Shit! <b>❌ ꜰʟᴏᴏᴅ ʙᴇᴋʟᴇᴍᴇ ʜᴀᴛᴀꜱɪ ❌ \n ᴜᴢɢᴜɴᴜᴍ! ᴋᴜʟʟᴀɴɪᴄɪ {user.first_name} ʏᴏɢᴜɴ ᴋᴀᴛɪʟɪᴍ ɪꜱᴛᴇᴋʟᴇʀɪ ɴᴇᴅᴇɴɪʏʟᴇ ɢʀᴜʙᴜɴᴜᴢᴀ ᴋᴀᴛɪʟᴀᴍᴀᴅɪ! ᴀʏʀɪᴄᴀ, ɢʀᴜʙᴜɴᴜᴢᴅᴀ ʏᴀʏɪɴᴄɪ ʜᴇꜱᴀʙɪɴɪɴ ʏᴀꜱᴀᴋʟᴀɴᴍᴀᴅɪɢɪɴᴅᴀɴ ᴇᴍɪɴ ᴏʟᴜɴ. ✅"
            "\n\nᴠᴇʏᴀ ᴍᴀɴᴜᴇʟ ᴏʟᴀʀᴀᴋ ᴇᴋʟᴇʏᴇʙɪʟɪʀꜱɪɴɪᴢ @{(await USER.get_me()).username} ɢʀᴜʙᴜɴᴜᴢᴀ!</b> 😉",
        )
        return
    await message.reply_text(
            "<b>Streamer Account Joined</b> 😊",
        )

# Remove Bot and Streamer Account From the group
@Client.on_message(filters.group & filters.command(["leavegrp"]))
@authorized_users_only
async def botleavegrp(client, message):
    await message.chat.leave()

@USER.on_message(filters.group & filters.command(["leavegrp"]))
async def strmleavegrp(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Oops! ʏᴀʏɪɴᴄɪ ʜᴇꜱᴀʙɪ ꜱᴜ ᴀɴᴅᴀ ᴀʏʀɪʟᴀᴍɪʏᴏʀ! ꜰʟᴏᴏᴅᴡᴀɪᴛ ᴏʟᴀʙɪʟɪʀ 🤔"
            "\n\nᴠᴇʏᴀ ᴇʟ ɪʟᴇ ᴋᴀʟᴅɪʀᴀʙɪʟɪʀꜱɪɴɪᴢ @{(await USER.get_me()).username} 🤗</b>",
        )
        return
