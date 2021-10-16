from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from callsmusic.callsmusic import client as USER
from config import BOT_USERNAME, UPDATES_CHANNEL

# close calllback

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

# Player Control Callbacks

@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**ɪꜱᴛᴇ ꜱᴛʀᴇᴀᴍᴇʀ'ɪɴ ᴋᴏɴᴛʀᴏʟ ᴍᴇɴᴜꜱᴜ!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ ᴅᴜʀᴀᴋʟᴀᴛ ⏸", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ ᴅᴇᴠᴀᴍ ᴇᴛ ▶️", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ ᴀᴛʟᴀ ⏩", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ ʙɪᴛɪʀ ⏹", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔇 ꜱᴇꜱꜱɪᴢ 🔇", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "🔈 ꜱᴇꜱɪɴɪ ᴀᴄᴍᴀᴋ 🔈", callback_data="cbunmute"
                    )
                ]
            ]
        )
    )


# Start callback 

@Client.on_callback_query(filters.regex("cbstart"))
async def startcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hi {query.message.from_user.mention} 😉️!</b>

ʙᴇɴ ᴊᴀᴄᴋᴍᴇᴅʏᴀ ᴍᴜᴢɪᴋ ʙᴏᴛᴜʏᴜᴍ! ɢʀᴜᴘ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇ ᴍᴜᴢɪᴋ ᴄᴀʟᴍᴀᴋ ɪᴄɪɴ ɢᴜᴄʟᴜ ʙɪʀ ʙᴏᴛ 😇!

ᴀʏʀɪᴄᴀ ᴅᴀʜᴀ ꜰᴀᴢʟᴀ ᴏᴢᴇʟʟɪɢɪᴍ ᴠᴀʀ! ᴍᴇɴᴜʏᴜ ɢᴏʀ **/help** ʏᴀᴢᴀʀᴀᴋ ɢᴏʀᴇʙɪʟɪʀꜱɪɴɪᴢ 😘!

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
    

# Help Callback Menu

@Client.on_callback_query(filters.regex("cbhelpmenu"))
async def cbhelpmenu(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hi {query.message.from_user.mention} 😉️!</b>

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
                        "ꜱᴀʀᴋɪ ꜱᴏᴢʟᴇʀɪ ᴀʟ", callback_data="cbgetlyrics"
                    ),
                    InlineKeyboardButton(
                        "ʏᴛ ᴀʀᴀᴍᴀ", callback_data="cbytsearch"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴍᴜᴢɪᴋ ɪɴᴅɪʀɪᴄɪ", callback_data="cbmusicdown"
                    ),
                    InlineKeyboardButton(
                        "ʏᴛ ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪᴄɪ", callback_data="cbytviddown"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴋᴏᴍᴜᴛʟᴀʀɪ ꜱɪʟ", callback_data="cbdelcmds"
                    ),
                    InlineKeyboardButton(
                        "ᴀʟɪɴᴛɪ ᴏʟᴀʀᴀᴋ", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )

# How to Use Module Help

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbhowtouse(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ʙᴜ ʙᴏᴛ ɴᴀꜱɪʟ ᴋᴜʟʟᴀɴɪʟɪʀ?</b>

**ʙᴏᴛ ᴋᴜʀᴜʟᴜᴍᴜ:**
    1. ᴇᴋʟᴇ **{BOT_USERNAME}** ʙᴏᴛ ᴠᴇ @{(await USER.get_me()).username} ɢʀᴜʙᴜɴᴜᴢᴀ! (ɢᴏɴᴅᴇʀ `/joingrp` ɢʀᴜʙᴜɴᴜᴢᴀ! ʏᴀʏɪɴᴄɪ ᴏᴛᴏᴍᴀᴛɪᴋ ᴏʟᴀʀᴀᴋ ᴋᴀᴛɪʟᴀᴄᴀᴋ)
    2. Give Admin To **{BOT_USERNAME}** and **@{(await USER.get_me()).username}** !

 
**ᴏʏᴜɴᴄᴜ ᴋᴏᴍᴜᴛʟᴀʀɪɴɪ ᴋᴜʟʟᴀɴᴍᴀ:**
    1. **ʏᴀʟɴɪᴢᴄᴀ ɢʀᴜᴘ ʏᴏɴᴇᴛɪᴄɪꜱɪ ᴋᴏᴍᴜᴛʟᴀʀɪ 👮 ,**
     - `/play` - ᴅᴇꜱᴛᴇᴋʟᴇɴᴇɴ ᴜʀʟ'ʏɪ ʏᴀɴɪᴛʟᴀ, ꜱᴇꜱ ᴅᴏꜱʏᴀꜱɪɴɪ ʏᴀɴɪᴛʟᴀ ᴠᴇʏᴀ ɢᴏɴᴅᴇʀ `/play` ɪʟᴇ ʙɪʀʟɪᴋᴛᴇ [ᴅᴇꜱᴛᴇᴋʟᴇɴᴇɴ ᴜʀʟ](https://ytdl-org.github.io/youtube-dl/supportedsites.html)
       **ᴏʀɴᴇᴋ:** `/play https://www.youtube.com/watch?v=ALZHF5UqnU4`
        
     - `/nplay` - ꜱᴀʀᴋɪʏɪ ᴀᴅɪɴᴀ ɢᴏʀᴇ ᴄᴀʟ. (ꜱᴜ ᴀɴᴅᴀ ʏᴀʟɴɪᴢᴄᴀ ʏᴏᴜᴛᴜʙᴇ ɪᴄɪɴ ᴅᴇꜱᴛᴇᴋʟᴇɴɪʏᴏʀ)
       **ᴏʀɴᴇᴋ:** `/nplay faded`
    
     - `/skip` - ꜱᴜ ᴀɴᴅᴀ ᴄᴀʟᴍᴀᴋᴛᴀ ᴏʟᴀɴ ꜱᴀʀᴋɪʏɪ ᴀᴛʟᴀ.
    
     - `/pause` - ꜱᴜ ᴀɴᴅᴀ ᴄᴀʟᴍᴀᴋᴛᴀ ᴏʟᴀɴ ꜱᴀʀᴋɪʏɪ ᴅᴜʀᴀᴋʟᴀᴛ.
    
     - `/resume` - ꜱᴜ ᴀɴᴅᴀ ᴀᴋᴛᴀʀɪʟᴀɴ ꜱᴀʀᴋɪʏɪ ᴅᴇᴠᴀᴍ ᴇᴛᴛɪʀ.
    
     - `/mute` - ʏᴀʏɪɴᴄɪɴɪɴ ꜱᴇꜱɪɴɪ ᴋᴀᴘᴀᴛɪʀ.
    
     - `/unmute`- ʏᴀʏɪɴᴄɪɴɪɴ ꜱᴇꜱɪɴɪ ᴀᴄᴀʀ.
     
     - `/end` - ᴏʏɴᴀᴛᴍᴀʏɪ ʙɪʀᴀᴋɪʀ ᴠᴇ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛᴛᴇɴ ᴄɪᴋᴀʀ.
    
     - `/joingrp` - ɢʀᴜʙᴜɴᴜᴢᴀ ʏᴀʏɪɴᴄɪ ʜᴇꜱᴀʙɪ ᴇᴋʟᴇᴍᴇᴋ ɪᴄɪɴ.
    
     - `/leavegrp` - ʏᴀʏɪɴᴄɪ ʜᴇꜱᴀʙɪɴɪ ɢʀᴜʙᴜɴᴜᴢᴅᴀɴ ᴋᴀʟᴅɪʀᴍᴀᴋ ɪᴄɪɴ.
     
     - `/control` - ʏᴀʏɪɴᴄɪɴɪɴ ʜᴇꜱᴀʙɪɴɪ ᴅᴜɢᴍᴇʟᴇʀʟᴇ ᴋᴏɴᴛʀᴏʟ ᴇᴛᴍᴇᴋ ɪᴄɪɴ. (Like pause, resume, skip etc.)
     
    2. **ᴅɪɢᴇʀ ᴋᴏᴍᴜᴛʟᴀʀ,**
     - `/vc` - ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛ ʙᴀɢʟᴀɴᴛɪꜱɪɴɪ ᴀʟᴍᴀᴋ ᴠᴇ ᴘᴀʏʟᴀꜱᴍᴀᴋ ɪᴄɪɴ. (ʏᴀʟɴɪᴢᴄᴀ ʜᴇʀᴋᴇꜱᴇ ᴀᴄɪᴋ ɢʀᴜᴘʟᴀʀ)


**ᴅᴇꜱᴛᴇᴋʟᴇɴᴇɴ ᴜʀʟ ʟɪꜱᴛᴇꜱɪ:** https://ytdl-org.github.io/youtube-dl/supportedsites.html

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴅᴇꜱᴛᴇᴋʟᴇɴᴇɴ ᴜʀʟ ʟɪꜱᴛᴇꜱɪ", url="https://ytdl-org.github.io/youtube-dl/supportedsites.html"
                    ),
                    InlineKeyboardButton(
                        "◀️ ɢᴇʀɪ ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        ),
        disable_web_page_preview = True
    )


# Lyrics Module Help

@Client.on_callback_query(filters.regex("cbgetlyrics"))
async def cbgetlyrics(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Lyrics Plugin</b>

**ᴏᴢᴇʟʟɪᴋ:** ꜱᴀɢʟᴀɴᴀɴ ꜱᴀʀᴋɪ ᴀᴅɪ ɪᴄɪɴ ꜱᴏᴢ ᴀʟ!

**ᴋᴜʟʟᴀɴɪᴍ:**
    - ɪʟᴇ ꜱᴀʀᴋɪ ᴀᴅɪɴɪᴢɪ ɢᴏɴᴅᴇʀɪɴ `/lyrics` ᴇᴍʀᴇᴛᴍᴇᴋ.

**ᴏʀɴᴇᴋ:** `/lyrics faded`

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ ɢᴇʀɪ ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Yt Search Module Help

@Client.on_callback_query(filters.regex("cbytsearch"))
async def cbytsearch(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ʏᴛ ᴀʀᴀᴍᴀ ᴇᴋʟᴇɴᴛɪꜱɪ ɪᴄɪɴ ʏᴀʀᴅɪᴍ</b>

**ᴏᴢᴇʟʟɪᴋ:** ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏʟᴀʀɪɴɪ ꜱᴀᴛɪʀ ɪᴄɪ ᴏʟᴀʀᴀᴋ ᴠᴇʏᴀ ʙɪʀ ᴋᴏᴍᴜᴛ ᴋᴜʟʟᴀɴᴀʀᴀᴋ ᴀʀᴀʏɪɴ!

**ᴋᴜʟʟᴀɴɪᴍ:**
    1. ꜱᴀᴛɪʀ ɪᴄɪ ᴀʀᴀᴍᴀ ɪᴄɪɴ ᴏᴢᴇʟʟɪᴋ,
     - ᴛɪᴘ `@{BOT_USERNAME}` ʜᴇʀʜᴀɴɢɪ ʙɪʀ ꜱᴏʜʙᴇᴛᴛᴇ ʏᴀᴢɪɴ ` `(space) ᴠᴇ ᴀʀᴀᴍᴀ.
    
    2. ᴋᴏᴍᴜᴛ ʏᴏʟᴜʏʟᴀ ᴀʀᴀᴍᴀ ɪᴄɪɴ,
     - ɢᴏɴᴅᴇʀ `/ytsearch` ᴀɴᴀʜᴛᴀʀ ᴋᴇʟɪᴍᴇɴɪᴢʟᴇ ᴋᴏᴍᴜᴛ ᴠᴇʀɪɴ.

**ᴏʀɴᴇᴋ:**
    1. ꜱᴀᴛɪʀ ɪᴄɪ ᴀʀᴀᴍᴀ ɪᴄɪɴ ᴏʀɴᴇᴋ
     - `@{BOT_USERNAME} faded`
    
    2. ᴋᴏᴍᴜᴛ ʏᴏʟᴜʏʟᴀ ᴀʀᴀᴍᴀ ᴏʀɴᴇɢɪ
     - `/ytsearch faded`

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ ɢᴇʀɪ ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
    
    
# Music Downloader Help

@Client.on_callback_query(filters.regex("cbmusicdown"))
async def cbmusicdown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ᴍᴜᴢɪᴋ ɪɴᴅɪʀɪᴄɪ ᴇᴋʟᴇɴᴛɪꜱɪ ʏᴀʀᴅɪᴍɪ</b>

**ᴏᴢᴇʟʟɪᴋ:** ʏᴏᴜᴛᴜʙᴇ, ꜱᴀᴀᴠɴ, ᴅᴇᴇᴢᴇʀ'ᴅᴀɴ ᴍᴜᴢɪᴋ ᴏʟᴀʀᴀᴋ ꜱᴇꜱ ɪɴᴅɪʀɪɴ

**ᴋᴜʟʟᴀɴɪᴍ:**
    1. ʏᴏᴜᴛᴜʙᴇ ꜱᴇꜱ ɪɴᴅɪʀᴍᴇᴋ ɪᴄɪɴ,
      - ꜱᴀʀᴋɪ ᴀᴅɪɴɪᴢɪ ɢᴏɴᴅᴇʀɪɴ `/yts` ᴇᴍʀᴇᴛᴍᴇᴋ.
    
    2. ꜱᴀᴀᴠɴ ꜱᴇꜱ ɪɴᴅɪʀᴍᴇᴋ ɪᴄɪɴ,
      - ꜱᴀʀᴋɪ ᴀᴅɪɴɪᴢɪ ɢᴏɴᴅᴇʀɪɴ `/saavn` ᴇᴍʀᴇᴛᴍᴇᴋ.
    
    3. ᴅᴇᴇᴢᴇʀ ꜱᴇꜱ ɪɴᴅɪʀᴍᴇ ɪᴄɪɴ,
      - ꜱᴀʀᴋɪ ᴀᴅɪɴɪᴢɪ ɢᴏɴᴅᴇʀɪɴ `/deezer` ᴇᴍʀᴇᴛᴍᴇᴋ.

**ᴏʀɴᴇᴋ:**
    1. ʏᴏᴜᴛᴜʙᴇ ꜱᴇꜱ ɪɴᴅɪʀᴍᴇ ᴏʀɴᴇɢɪ,
      - `/yts alone`
    
    2. ꜱᴀᴀᴠɴ ꜱᴇꜱ ɪɴᴅɪʀᴍᴇ ᴏʀɴᴇɢɪ,
      - `/saavn faded`
    
    3. ᴅᴇᴇᴢᴇʀ ꜱᴇꜱ ɪɴᴅɪʀᴍᴇ ᴏʀɴᴇɢɪ,
      - `/deezer unity`

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ ɢᴇʀɪ ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# YT Video Downloader Help

@Client.on_callback_query(filters.regex("cbytviddown"))
async def cbytviddown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ʏᴛ ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪᴄɪ ᴇᴋʟᴇɴᴛɪꜱɪ ɪᴄɪɴ ʏᴀʀᴅɪᴍ</b>

**Özellik:** ꜱᴀɢʟᴀɴᴀɴ ᴀᴅ ɪᴄɪɴ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏʟᴀʀɪɴɪ ɪɴᴅɪʀɪɴ!

**ᴋᴜʟʟᴀɴɪᴍ:**
    - ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴀᴅɪɴɪᴢɪ ɪʟᴇ ɢᴏɴᴅᴇʀɪɴ `/ytvid` ᴇᴍʀᴇᴛᴍᴇᴋ.

**ᴏʀɴᴇᴋ:** `/ytvid faded`

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ ɢᴇʀɪ ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Delete Command Help

@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ᴋᴏᴍᴜᴛ ᴇᴋʟᴇɴᴛɪꜱɪɴɪ ꜱɪʟᴍᴇ ʏᴀʀᴅɪᴍɪ</b>

**ᴏᴢᴇʟʟɪᴋ:** ɢʀᴜʙᴜɴᴜᴢᴅᴀ ɪꜱᴛᴇɴᴍᴇʏᴇɴ ᴘᴏꜱᴛᴀʟᴀʀɪ ᴏɴʟᴇᴍᴇᴋ ɪᴄɪɴ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀ ᴛᴀʀᴀꜰɪɴᴅᴀɴ ɢᴏɴᴅᴇʀɪʟᴇɴ ᴛᴜᴍ ᴋᴏᴍᴜᴛʟᴀʀɪ ꜱɪʟɪɴ!

**ᴋᴜʟʟᴀɴɪᴍ:**
    1. ʙᴜɴᴜ ᴀᴄᴍᴀᴋ ɪᴄɪɴ,
      - ɢᴏɴᴅᴇʀᴍᴇᴋ `/delcmd on` ᴇᴍʀᴇᴛᴍᴇᴋ.
    
    2. ʙᴜɴᴜ ᴋᴀᴘᴀᴛᴍᴀᴋ ɪᴄɪɴ,
      - ɢᴏɴᴅᴇʀᴍᴇᴋ `/delcmd off` ᴇᴍʀᴇᴛᴍᴇᴋ.

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ ɢᴇʀɪ ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Quotely Help

@Client.on_callback_query(filters.regex("cbquotely"))
async def cbquotely(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Qᴜᴏᴛᴇʟʏ ᴇᴋʟᴇɴᴛɪꜱɪ ɪᴄɪɴ ʏᴀʀᴅɪᴍ</b>

**ᴏᴢᴇʟʟɪᴋ:** Qᴜᴏᴛᴇʟʏ ʙᴏᴛ ɢɪʙɪ ᴀʟɪɴᴛɪ ᴍᴇꜱᴀᴊʟᴀʀɪ!

**ᴋᴜʟʟᴀɴɪᴍ:**
    1. ʙɪʀ ᴍᴇꜱᴀᴊɪ ᴀʟɪɴᴛɪʟᴀᴍᴀᴋ,
      - `/q` ʙɪʀ ᴍᴇᴛɪɴ ᴍᴇꜱᴀᴊɪɴᴀ ᴄᴇᴠᴀᴘ ᴠᴇʀᴍᴇᴋ
      
    2. ʙɪʀᴅᴇɴ ꜰᴀᴢʟᴀ ᴍᴇꜱᴀᴊ ᴀʟɪɴᴛɪʟᴀᴍᴀᴋ,
      - `/q` [Integer] ʙɪʀ ᴍᴇᴛɪɴ ᴍᴇꜱᴀᴊɪɴᴀ ᴄᴇᴠᴀᴘ ᴠᴇʀᴍᴇᴋ
     
    3. ᴄᴇᴠᴀᴘʟɪ ᴍᴇꜱᴀᴊɪ ᴀʟɪɴᴛɪʟᴀᴍᴀᴋ ɪᴄɪɴ
      - `/q r` ʙɪʀ ᴍᴇᴛɪɴ ᴍᴇꜱᴀᴊɪɴᴀ ᴄᴇᴠᴀᴘ ᴠᴇʀᴍᴇᴋ

**ᴏʀɴᴇᴋ:**
    1. ᴏʀɴᴇᴋ ᴀʟɪɴᴛɪ ʙɪʀ ᴍᴇꜱᴀᴊ,
      - `/q` ʙɪʀ ᴍᴇᴛɪɴ ᴍᴇꜱᴀᴊɪɴᴀ ᴄᴇᴠᴀᴘ ᴠᴇʀᴍᴇᴋ
      
    2. ᴏʀɴᴇᴋ ᴀʟɪɴᴛɪ ʙɪʀᴅᴇɴ ꜰᴀᴢʟᴀ ᴍᴇꜱᴀᴊ,
      - `/q 2` ʙɪʀ ᴍᴇᴛɪɴ ᴍᴇꜱᴀᴊɪɴᴀ ᴄᴇᴠᴀᴘ ᴠᴇʀᴍᴇᴋ
     
    3. ᴄᴇᴠᴀᴘʟɪ ᴏʀɴᴇᴋ ᴀʟɪɴᴛɪ ᴍᴇꜱᴀᴊɪ,
      - `/q r` ʙɪʀ ᴍᴇᴛɪɴ ᴍᴇꜱᴀᴊɪɴᴀ ᴄᴇᴠᴀᴘ ᴠᴇʀᴍᴇᴋ

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ ɢᴇʀɪ ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
