import os

from pyrogram import Client, filters # Ik this is weird as this shit is already imported in line 6! anyway ... Fuck Off!
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2
from helpers.database import db, Database
from helpers.dbthings import handle_user_status
from config import LOG_CHANNEL, BOT_USERNAME, UPDATES_CHANNEL


@Client.on_message(filters.private)
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/start":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **ᴋᴜʟʟᴀɴᴍᴀʏᴀ ʙᴀꜱʟᴀᴅɪᴍ!** \n\nɪʟᴋ ᴀᴅɪ: `{message.from_user.first_name}` \nᴜꜱᴇʀ ɪᴅ: `{message.from_user.id}` \nᴘʀᴏꜰɪʟᴇ ʟɪɴᴋ: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention} 😉️!</b>

ʙᴇɴ ᴊᴀᴄᴋᴍᴇᴅʏᴀ ᴍᴜᴢɪᴋ ʙᴏᴛᴜʏᴜᴍ! ɢʀᴜᴘ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇ ᴍᴜᴢɪᴋ ᴄᴀʟᴍᴀᴋ ɪᴄɪɴ ɢᴜᴄʟᴜ ʙɪʀ ʙᴏᴛ 😇!

ᴀʏʀɪᴄᴀ ᴅᴀʜᴀ ꜰᴀᴢʟᴀ ᴏᴢᴇʟʟɪɢɪᴍ ᴠᴀʀ! ʟᴜᴛꜰᴇɴ ᴋᴏᴍᴜᴛᴜ ʏᴀᴢ **/help** ᴋᴏᴍᴜᴛʟᴀʀɪ ɢᴏʀ 😘!

Made with ❤️ **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👮‍♂️ ʏᴀʀᴅɪᴍ ᴍᴇɴᴜꜱᴜ 👮‍♂️", callback_data="cbhelpmenu"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📦 ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ 📦", url="https://github.com/newname58q"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ ɢᴜɴᴄᴇʟʟᴇᴍᴇ ᴋᴀɴᴀʟɪᴍ 🔰️", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "⚜️ ᴅᴇꜱᴛᴇᴋ ɢʀᴜʙᴜ ⚜️", url="https://t.me/jackmedyaa"
                    )
                ]
            ]
        )
    )


# Help Menu

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def help(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/help":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **ᴋᴜʟʟᴀɴᴍᴀʏᴀ ʙᴀꜱʟᴀᴅɪᴍ!** \n\nɪʟᴋ ᴀᴅɪ: `{message.from_user.first_name}` \nᴜꜱᴇʀ ɪᴅ: `{message.from_user.id}` \nᴘʀᴏꜰɪʟᴇ ʟɪɴᴋ: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention} 😉️!</b>

**ɪꜱᴛᴇ ʙᴜ ʙᴏᴛ ɪᴄɪɴ ʏᴀʀᴅɪᴍ ᴍᴇɴᴜꜱᴜ 😊!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤔 ʙᴇɴɪ ɴᴀꜱɪʟ ᴋᴜʟʟᴀɴɪʀꜱɪɴ 🤔", callback_data="cbhowtouse"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Get Lyrics", callback_data="cbgetlyrics"
                    ),
                    InlineKeyboardButton(
                        "YT Search", callback_data="cbytsearch"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Music Downloader", callback_data="cbmusicdown"
                    ),
                    InlineKeyboardButton(
                        "YT Video Downloader", callback_data="cbytviddown"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Delete Commands", callback_data="cbdelcmds"
                    ),
                    InlineKeyboardButton(
                        "Quotely", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/credits":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **ᴋᴜʟʟᴀɴᴍᴀʏᴀ ʙᴀꜱʟᴀᴅɪᴍ!** \n\nɪʟᴋ ᴀᴅɪ: `{message.from_user.first_name}` \nᴜꜱᴇʀ ɪᴅ: `{message.from_user.id}` \nᴘʀᴏꜰɪʟᴇ ʟɪɴᴋ: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

__Note!__ ⚠️: ʙᴜ ᴘʀᴏᴊᴇ <b>ᴛᴀᴍᴀᴍᴇɴ ʙᴀɴᴀ ᴀɪᴛ ᴅᴇɢɪʟ</b> !

Credits To,

<b><a href="https://github.com/newname58q">JackMedyaMusic</a></b> - For JackMedyaMusic (Main Code ❤️) !
<b>JackMedya</b>
<b>JackMedya</b>
<b>JackMedya</b>
<b>JackMedya</b>
<b>JackMedya</b>
<b>JackMedya</b>

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ ɢᴜɴᴄᴇʟʟᴇᴍᴇ ᴋᴀɴᴀʟɪᴍ 🔰️", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ ᴅᴇꜱᴛᴇᴋ ɢʀᴜʙᴜ ⚜️", url="https://t.me/jackmedyaa"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )   


@Client.on_message(command(["vc", f"vc@{BOT_USERNAME}"]) & other_filters)
async def vc(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/vc":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **ᴋᴜʟʟᴀɴᴍᴀʏᴀ ʙᴀꜱʟᴀᴅɪᴍ!** \n\nɪʟᴋ ᴀᴅɪ: `{message.from_user.first_name}` \nᴜꜱᴇʀ ɪᴅ: `{message.from_user.id}` \nᴘʀᴏꜰɪʟᴇ ʟɪɴᴋ: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    VC_LINK = f"https://t.me/{message.chat.username}?voicechat"
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>


             😌️  **ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛ ʙᴀɢʟᴀɴᴛɪꜱɪ** 😌️
____________________------------______________________

👉️ [ɪꜱᴛᴇ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛ ʙᴀɢʟᴀɴᴛɪɴɪᴢ](https://t.me/{message.chat.username}?voicechat) 👈️
____________________------------______________________

Enjoy 😌️❤️!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "↗️ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛ ᴅᴀᴠᴇᴛɪʏᴇꜱɪ ↗️", url=f"https://t.me/share/url?url=**Join%20Our%20Group%20Voice%20Chat%20😉%20%20{VC_LINK}%20❤️**"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ ᴋᴀɴᴀʟɪ ɢᴜɴᴄᴇʟʟᴇ 🔰️", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "⚜️ ᴅᴇꜱᴛᴇᴋ ɢʀᴜʙᴜ ⚜️", url="https://t.me/jackmedyaa"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )

    
@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def search(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/search":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **ᴋᴜʟʟᴀɴᴍᴀʏᴀ ʙᴀꜱʟᴀᴅɪᴍ!** \n\nɪʟᴋ ᴀᴅɪ: `{message.from_user.first_name}` \nᴜꜱᴇʀ ɪᴅ: `{message.from_user.id}` \nᴘʀᴏꜰɪʟᴇ ʟɪɴᴋ: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        "💁🏻‍♂️ ʙɪʀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏꜱᴜ ᴀʀᴀᴍᴀᴋ ɪꜱᴛɪʏᴏʀ ᴍᴜꜱᴜɴᴜᴢ??",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ ᴇᴠᴇᴛ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "ʜᴀʏɪʀ ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
