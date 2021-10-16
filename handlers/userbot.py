# Copyright (c) 2021 @Bruh_0x (Itz-fork) <https://github.com/Itz-fork>
# Made with ❤️ for CallsMusic-Plus <https://github.com/Itz-fork/Callsmusic-Plus>
# Kanging without credits is strictly prohibited

import heroku3
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message

from config import BOT_USERNAME, BOT_OWNER, cp_version, nexaub_version
from callsmusic.callsmusic import client as NEXAUB
from handlers.ownerstuff import _check_heroku

# To Block a PM'ed User
@NEXAUB.on_message(filters.private & filters.command("block", [".", "/"]) & filters.me & ~filters.edited)
async def ubblock(_, message: Message):
  shit_id = message.chat.id
  gonna_block_u = await message.edit_text("`ᴋᴜʟʟᴀɴɪᴄɪʏɪ ᴇɴɢᴇʟʟᴇᴍᴇ...`")
  try:
    await NEXAUB.block_user(shit_id)
    await gonna_block_u.edit("`ʙᴜ ᴋᴜʟʟᴀɴɪᴄɪ ʙᴀꜱᴀʀɪʏʟᴀ ᴇɴɢᴇʟʟᴇɴᴅɪ`")
  except Exception as lol:
    await gonna_block_u.edit(f"`ʙᴜ ᴋᴜʟʟᴀɴɪᴄɪʏɪ ᴇɴɢᴇʟʟᴇʏᴇᴍɪʏᴏʀᴜᴍ! ʙᴜ ʏᴇᴛᴋɪʟɪ ᴏʟᴀʙɪʟɪʀ ᴍɪ?` \n\n**ʜᴀᴛᴀ:** `{lol}`")


# To Unblock User That Already Blocked
@NEXAUB.on_message(filters.command("unblock", [".", "/"]) & filters.me & ~filters.edited)
async def ubblock(_, message: Message):
  good_bro = int(message.command[1])
  gonna_unblock_u = await message.edit_text("`ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ᴇɴɢᴇʟɪɴɪ ᴋᴀʟᴅɪʀᴍᴀ...`")
  try:
    await NEXAUB.unblock_user(good_bro)
    await gonna_unblock_u.edit(f"`ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ᴇɴɢᴇʟɪ ʙᴀꜱᴀʀɪʏʟᴀ ᴋᴀʟᴅɪʀɪʟᴅɪ` \n**ᴜꜱᴇʀ ɪᴅ:** `{good_bro}`")
  except Exception as lol:
    await gonna_unblock_u.edit(f"`ᴏ ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ᴇɴɢᴇʟɪɴɪ ᴋᴀʟᴅɪʀᴀᴍɪʏᴏʀᴜᴍ!, ʙᴇɴᴄᴇ ʜᴀʟᴀ ᴇɴɢᴇʟʟɪ!` \n\n**ʜᴀᴛᴀ:** `{lol}`")


# To Get How Many Chats that you are in (PM's also counted)
@NEXAUB.on_message(filters.private & filters.command("chats", [".", "/"]) & filters.me & ~filters.edited)
async def ubgetchats(_, message: Message):
  getting_chats = await message.edit_text("`ꜱᴏʜʙᴇᴛʟᴇʀɪɴɪᴢɪ ᴋᴏɴᴛʀᴏʟ ᴇᴅɪɴ, ʙᴇᴋʟᴇʏɪɴ...`")
  async for dialog in NEXAUB.iter_dialogs():
    try:
      total = await NEXAUB.get_dialogs_count()
      await getting_chats.edit(f"**ꜱᴀʏɪʟᴀɴ ᴛᴏᴘʟᴀᴍ ɪʟᴇᴛɪꜱɪᴍ ᴋᴜᴛᴜꜱᴜ:** `{total}` \n\n**ᴋᴀʀᴀʀʟɪ ᴅᴇɢɪʟ**")
    except Exception as lol:
      brokenmsg = await message.reply_text(f"`ꜱᴇɴᴅᴇɴ ᴀꜱʟᴀ ᴠᴀᴢɢᴇᴄᴍᴇʏᴇᴄᴇɢɪᴍ!, ᴀᴍᴀ ʙɪʀ ꜱᴇʏʟᴇʀ ᴛᴇʀꜱ ɢɪᴛᴛɪ!`")
      await brokenmsg.edit(f"**ʜᴀᴛᴀ:** `{lol}`")


# Leave From a Chat
@NEXAUB.on_message(filters.command("kickme", [".", "/"]) & filters.me & ~filters.edited)
async def ubkickme(_, message: Message):
  i_go_away = await message.edit_text("`ʙᴜ ꜱᴏʜʙᴇᴛᴛᴇɴ ᴀʏʀɪʟᴍᴀᴋ...`")
  try:
    await NEXAUB.leave_chat(message.chat.id)
    await i_go_away.edit("`ʙᴜ ꜱᴏʜʙᴇᴛᴛᴇɴ ʙᴀꜱᴀʀɪʏʟᴀ ᴀʏʀɪʟᴅɪ!`")
  except Exception as lol:
    await i_go_away.edit(f"`ʙᴜ ꜱᴏʜʙᴇᴛᴛᴇɴ ᴄɪᴋᴀᴍɪʏᴏʀᴜᴍ!, ɴᴇ ᴀᴄɪᴍᴀꜱɪᴢ ʙɪʀ ᴅᴜɴʏᴀ!` \n\n**ʜᴀᴛᴀ:** `{lol}`")


# Alive Message
@NEXAUB.on_message(filters.command("alive", [".", "/"]) & filters.me & ~filters.edited)
async def ubalive(_, message: Message):
  alive_msg = await message.edit_text("`ɪꜱʟᴇɴɪʏᴏʀ...`")
  alive_pic = "cache/NexaUB.jpg"
  await message.reply_photo(alive_pic, caption=f"**🌀 ᴊᴀᴄᴋᴍᴇᴅʏᴀ ᴍᴜꜱɪᴄ ᴋᴜʟʟᴀɴɪᴄɪ ʙᴏᴛᴜ ʏᴀꜱɪʏᴏʀ 🌀** \n\n**🤖 ᴠᴇʀꜱɪᴏɴ** \n ↳**ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ:** `{cp_version}` \n ↳**ᴜꜱᴇʀʙᴏᴛ ᴠᴇʀꜱɪᴏɴ:** `{nexaub_version}` \n\n**🐬 ɪɴꜰᴏ**\n ↳**ᴍᴜꜱɪᴄ ʙᴏᴛ:** @{BOT_USERNAME} \n ↳**ᴏᴡɴᴇʀ:** [Click Here](tg://user?id={BOT_OWNER})")
  await alive_msg.delete()


# Get Streamer's Private Chat Messages in to a Private Group
PM_LOGS = os.environ.get("PM_LOGS", "")
PM_LOG_CHAT_ID = int(os.environ.get("PM_LOG_CHAT_ID", 12345678))

@NEXAUB.on_message(filters.private & filters.command("pmlogs", [".", "/"]) & filters.me & ~filters.edited)
@_check_heroku
async def getlogs(client: NEXAUB, message: Message, app_):
  if len(message.command) != 2:
        await message.edit_text("`ʙɪʀ ᴅᴀᴋɪᴋᴀ` \n\n**ᴀᴄᴍᴀᴋ ɪᴄɪɴ:** `.pmlogs on` \n**ᴋᴀᴘᴀᴛᴍᴀᴋ ɪᴄɪɴ:** `.pmlogs off` ")
        return
  status = message.text.split(None, 1)[1].strip()
  status = status.lower()
  if status == "on":
    if PM_LOG_CHAT_ID != 12345678:
      await message.edit("`ʙᴜɴᴜ ᴢᴀᴛᴇɴ ʏᴀᴘᴛɪɴ ɴᴇᴅᴇɴ ᴛᴇᴋʀᴀʀ?`")
      return # Next level logic lol
    logmsg = await message.edit_text("`ᴘᴍ ᴍᴇꜱᴀᴊ ɢᴜɴʟᴜᴋʟᴇʀɪ ᴍᴏᴅᴜʟᴜ ꜱɪᴍᴅɪ ʙᴀꜱʟɪʏᴏʀ...`")
    await asyncio.sleep(2) # Lmao
    chat_pic = "cache/NexaUB.jpg"
    try:
      await logmsg.edit("`ꜱɪᴍᴅɪ ᴏᴢᴇʟ ɢʀᴜᴘ ᴏʟᴜꜱᴛᴜʀᴍᴀ...`!")
      pmchat = await NEXAUB.create_group(f"ᴊᴀᴄᴋᴍᴇᴅʏᴀ ᴜꜱᴇʀʙᴏᴛ'ᴜɴ ᴘᴍ ɢᴜɴʟᴜᴋʟᴇʀɪ", BOT_OWNER)
      chat_id = pmchat.id
      await NEXAUB.set_chat_photo(chat_id=chat_id, photo=chat_pic)
      await logmsg.edit(f"`ᴀᴅɪᴍ 1 ʙᴀꜱᴀʀɪʏʟᴀ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ, ʙᴜ ᴏᴢᴇʟʟɪɢɪ ᴇᴛᴋɪɴʟᴇꜱᴛɪʀᴍᴇᴋ ɪᴄɪɴ ʟᴜᴛꜰᴇɴ ꜱɪᴍᴅɪ ᴏʟᴜꜱᴛᴜʀᴜʟᴀɴ ɢᴜɴʟᴜᴋ ɢʀᴜʙᴜɴᴜᴢᴜ ᴋᴏɴᴛʀᴏʟ ᴇᴅɪɴ!!` \n\n ~ **@JackmedyaBotsUpdates**")
      await client.send_message(chat_id, f"**ʜᴏꜱɢᴇʟᴅɪɴɪᴢ @{(await NEXAUB.get_me()).username}'s ᴘᴍ ɢᴜɴʟᴜᴋ ɢʀᴜʙᴜ!** \nʙᴜ ꜱᴏʜʙᴇᴛ ᴛᴜᴍ ᴘᴍ ᴍᴇꜱᴀᴊʟᴀʀɪɴɪ ɪᴄᴇʀᴇᴄᴇᴋᴛɪʀ **@{(await NEXAUB.get_me()).username}** ! \n\n\n`/setvar PM_LOG_CHAT_ID {chat_id}` \n\n ✪ **ʟᴜᴛꜰᴇɴ ʏᴜᴋᴀʀɪᴅᴀᴋɪ ᴋᴏᴍᴜᴛᴜ ᴋᴏᴘʏᴀʟᴀʏɪᴘ ɢᴏɴᴅᴇʀɪɴɪᴢ @{BOT_USERNAME} ꜱɪᴍᴅɪ**!")
    except Exception as lol:
      await logmsg.edit(f"`ʙᴜ ᴏᴢᴇʟʟɪᴋ ᴇᴛᴋɪɴʟᴇꜱᴛɪʀɪʟᴇᴍɪʏᴏʀ!, ʏᴀɴʟɪꜱ ʙɪʀ ꜱᴇʏ ᴏʟᴅᴜ!` \n\n**ʜᴀᴛᴀ:** `{lol}`")
      return
  elif status == "off":
    if PM_LOG_CHAT_ID == 12345678:
      await message.edit("`ɪʟᴋ ᴏɴᴄᴇ ʙᴜ ᴏᴢᴇʟʟɪɢɪ ᴇᴛᴋɪɴʟᴇꜱᴛɪʀɪɴ!`")
    heroku_var = app_.config()
    _var = "PM_LOG_CHAT_ID"
    try:
      await message.edit_text("`ᴘᴍ ɢᴜɴʟᴜᴋʟᴇʀɪ ᴏᴢᴇʟʟɪɢɪɴɪ ᴋᴀʟᴅɪʀᴍᴀʏᴀ ᴄᴀʟɪꜱᴍᴀᴋ...`")
      await NEXAUB.leave_chat(PM_LOG_CHAT_ID, delete=True)
      await message.edit_text("`ᴘᴍʟᴏɢ ɢʀᴜʙᴜɴᴅᴀɴ ᴀʏʀɪʟᴅɪ! ᴜᴍᴀʀɪᴍ ʙᴜ ᴅᴇᴠʀᴇ ᴅɪꜱɪ...`")
      heroku_var[_var] = 12345678
    except Exception as lol:
      await message.edit_text(f"`ʙᴜ ᴏᴢᴇʟʟɪᴋ ᴋᴀʟᴅɪʀɪʟᴀᴍɪʏᴏʀ! ʙᴇʟᴋɪ ᴇᴛᴋɪɴʟᴇꜱᴛɪʀᴍᴇᴅɪɴɪᴢ?` \n\n**ʜᴀᴛᴀ:** {lol}")


@NEXAUB.on_message(filters.private)
async def sendpmlol(client: NEXAUB, message: Message):
  NEXAUB_ID = int((await NEXAUB.get_me()).id)
  if message.from_user.id == BOT_OWNER or message.from_user.id == NEXAUB_ID:
    return
  pmlogchat = PM_LOG_CHAT_ID
  userinfo = await NEXAUB.get_users(user_ids=message.from_user.id)
  nibba = int(message.chat.id)
  msg_txt = message.text
  if PM_LOG_CHAT_ID == 12345678:
    return
  else:
    try:
      forwardedmsg = await client.forward_messages(chat_id=pmlogchat, from_chat_id=message.chat.id, message_ids=message.message_id)
      await forwardedmsg.reply_text(f"**ʙᴇᴋʟᴇɴᴍᴇʏᴇɴ ᴍᴇꜱᴀᴊ** \n\n**👤 ᴋᴜʟʟᴀɴɪᴄɪ ʙɪʟɢɪꜱɪ \n ⤷**ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ:** `{userinfo.first_name}` \n ⤷**ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ:** @{userinfo.username} \n ⤷**ᴜꜱᴇʀ ɪᴅ:** `{nibba}`", parse_mode="md")
    except Exception as lol:
      await client.send_message(chat_id=pmlogchat, text=f"`ᴍᴇꜱᴀᴊ ɢᴏɴᴅᴇʀɪʀᴋᴇɴ ʏᴀɴʟɪꜱ ʙɪʀ ꜱᴇʏ ᴏʟᴅᴜ!` \n\n**ʜᴀᴛᴀ:** {lol}", parse_mode="md")
