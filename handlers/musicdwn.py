# (c) @TheHamkerCat , @MrDarkPrince, @TeamOfDaisyX


from __future__ import unicode_literals


from urllib.parse import urlparse

import time
import os
import math
import asyncio
import aiofiles
import aiohttp
import ffmpeg
import requests
import wget
import youtube_dl

from asyncio import gather
from random import randint
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message,InlineKeyboardMarkup, InlineKeyboardButton
from youtubesearchpython import SearchVideos
from youtube_search import YoutubeSearch
from Python_ARQ import ARQ

from config import ARQ_API_URL, ARQ_API_KEY, BOT_USERNAME, UPDATES_CHANNEL
from helpers.merrors import capture_err
from helpers.modhelps import paste

is_downloading = False

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]

async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["▓" for i in range(math.floor(percentage / 10))]),
            "".join(["░" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


@Client.on_message(filters.command(['yts', f'yts@{BOT_USERNAME}']))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('**ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ! ꜱᴀʀᴋɪɴɪ ᴀʀɪʏᴏʀᴜᴍ 🔎...**')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "ꜱᴏʏʟᴇᴅɪɢɪᴍ ɪᴄɪɴ ᴜᴢɢᴜɴᴜᴍ ᴀᴍᴀ ʜɪᴄʙɪʀ ꜱᴇʏ ʙᴜʟᴀᴍɪʏᴏʀᴜᴍ ❌!\n\nʙᴀꜱᴋᴀ ʙɪʀ ᴀɴᴀʜᴛᴀʀ ᴋᴇʟɪᴍᴇ ᴅᴇɴᴇʏɪɴ! 🤔?"
        )
        print(str(e))
        return
    m.edit("**ꜱᴀʀᴋɪɴɪᴢɪ ɪɴᴅɪʀɪʏᴏʀᴜᴍ! ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ ⏰**")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎙 **Title**: [{title[:35]}]({link})\n🎬 **ᴋᴀʏɴᴀᴋ**: `YouTube`\n⏱️ **ꜱᴀʀᴋɪ ꜱᴜʀᴇꜱɪ**: `{duration}`\n👁‍🗨 **ꜱᴀʀᴋɪ ɢᴏʀᴜɴᴛᴜʟᴇᴍᴇ**: `{views}`\n\n**ʏᴜᴋʟᴇʏᴇɴ**: **@{BOT_USERNAME}** \n **ᴋᴀᴛɪʟᴍᴀᴋ @{UPDATES_CHANNEL} 😉** '
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


# Funtion To Download Song
async def download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


# Jiosaavn Music


@Client.on_message(filters.command(["saavn", f"saavn@{BOT_USERNAME}"]) & ~filters.edited)
@capture_err
async def jssong(_, message):
    global is_downloading
    if len(message.command) < 2:
        await message.reply_text("Command `/saavn` ʙɪʀ ᴀʀɢᴜᴍᴀɴ ɢᴇʀᴇᴋᴛɪʀɪʀ.")
        return
    if is_downloading:
        await message.reply_text(
            "Sorry! **ʙᴀꜱᴋᴀ ʙɪʀ ɪɴᴅɪʀᴍᴇ ɪꜱʟᴇᴍɪ ᴅᴇᴠᴀᴍ ᴇᴅɪʏᴏʀ !** ʙɪʀ ꜱᴜʀᴇ ꜱᴏɴʀᴀ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ!"
        )
        return
    is_downloading = True
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("**ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ! ꜱᴇɴɪɴ ꜱᴀʀᴋɪɴɪ ᴀʀɪʏᴏʀᴜᴍ 🔎...**")
    try:
        songs = await arq.saavn(query)
        if not songs.ok:
            await message.reply_text(songs.result)
            return
        sname = songs.result[0].song
        slink = songs.result[0].media_url
        ssingers = songs.result[0].singers
        await m.edit("**ꜱᴀʀᴋɪɴɪ ɪɴᴅɪʀɪʏᴏʀᴜᴍ! ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ ⏰**")
        song = await download_song(slink)
        await m.edit("**ꜱᴀʀᴋɪɴɪᴢɪ ʏᴜᴋᴇɴɪʏᴏʀ! ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ ⏰**")
        await message.reply_audio(
            audio=song,
            title=sname,
            performer=ssingers,
        )
        os.remove(song)
        await m.delete()
    except Exception as e:
        is_downloading = False
        await m.edit(str(e))
        return
    is_downloading = False


# Deezer Music


@Client.on_message(filters.command(["deezer", f"deezer@{BOT_USERNAME}"]) & ~filters.edited)
@capture_err
async def deezsong(_, message):
    global is_downloading
    if len(message.command) < 2:
        await message.reply_text("command `/deezer` ʙɪʀ ᴀʀɢᴜᴍᴀɴ ɢᴇʀᴇᴋᴛɪʀɪʀ.")
        return
    if is_downloading:
        await message.reply_text(
            "Sorry! **ʙᴀꜱᴋᴀ ʙɪʀ ɪɴᴅɪʀᴍᴇ ɪꜱʟᴇᴍɪ ᴅᴇᴠᴀᴍ ᴇᴅɪʏᴏʀ !** ʙɪʀ ꜱᴜʀᴇ ꜱᴏɴʀᴀ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ!"
        )
        return
    is_downloading = True
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("**ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ! ꜱᴀʀᴋɪɴɪ ᴀʀɪʏᴏʀᴜᴍ 🔎...**")
    try:
        songs = await arq.deezer(query, 1)
        if not songs.ok:
            await message.reply_text(songs.result)
            return
        title = songs.result[0].title
        url = songs.result[0].url
        artist = songs.result[0].artist
        await m.edit("**ꜱᴀʀᴋɪɴɪᴢɪ ɪɴᴅɪʀɪʏᴏʀᴜᴍ! ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ ⏰**")
        song = await download_song(url)
        await m.edit("**ꜱᴀʀᴋɪɴɪᴢɪ ʏᴜᴋʟᴇɴɪʏᴏʀ! ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ ⏰**")
        await message.reply_audio(
            audio=song,
            title=title,
            performer=artist,
        )
        os.remove(song)
        await m.delete()
    except Exception as e:
        is_downloading = False
        await m.edit(str(e))
        return
    is_downloading = False


# Song Lyrics


@Client.on_message(filters.command(["lyrics", f"lyrics@{BOT_USERNAME}"]))
async def lyrics_func(_, message):
    if len(message.command) < 2:
        await message.reply_text("**ʙᴜ ʏᴀɴʟɪꜱ ᴋᴏᴍᴜᴛ ᴋᴜʟʟᴀɴɪᴍɪ!** \nUse `/lyrics` (song name)")
        return
    m = await message.reply_text("**ꜱᴀʀᴋɪ ꜱᴏᴢʟᴇʀɪ ᴀʀᴀᴍᴀ**")
    query = message.text.strip().split(None, 1)[1]
    song = await arq.lyrics(query)
    lyrics = song.result
    if len(lyrics) < 4095:
        await m.edit(f"__{lyrics}__")
        return
    lyrics = await paste(lyrics)
    await m.edit(f"**Oops! ɢᴏɴᴅᴇʀᴍᴇᴋ ɪᴄɪɴ ᴄᴏᴋ ᴜᴢᴜɴ ꜱᴀʀᴋɪ ꜱᴏᴢʟᴇʀɪ!** \n**ꜱᴀʀᴋɪ ꜱᴏᴢʟᴇʀɪ: [Click Here]({lyrics})**")

# Youtube Video Download

@Client.on_message(filters.command(["ytvid", f"ytvid@{BOT_USERNAME}"]))
async def ytmusic(client, message: Message):
    global is_downloading
    if is_downloading:
        await message.reply_text(
            "Sorry! **ʙᴀꜱᴋᴀ ʙɪʀ ɪɴᴅɪʀᴍᴇ ɪꜱʟᴇᴍɪ ᴅᴇᴠᴀᴍ ᴇᴅɪʏᴏʀ !** ʙɪʀ ꜱᴜʀᴇ ꜱᴏɴʀᴀ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ!"
        )
        return

    urlissed = get_text(message)

    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} ʏᴏᴜᴛᴜʙᴇ ꜱᴜɴᴜᴄᴜʟᴀʀɪɴᴅᴀɴ. ʟᴜᴛꜰᴇɴ ʙɪʀᴀᴢ ʙᴇᴋʟᴇʏɪɴ!`"
    )
    if not urlissed:
        await pablo.edit("Invalid Command Syntax")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        is_downloading = True
        with youtube_dl.YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            duration = round(infoo["duration"] / 60)

            if duration > 999:
                await pablo.edit(
                    f"❌ 999 ᴅᴀᴋɪᴋᴀᴅᴀɴ ᴜᴢᴜɴ ᴠɪᴅᴇᴏʟᴀʀ(s) ɪᴢɪɴ ᴠᴇʀɪʟᴍᴇᴢ, ꜱᴀɢʟᴀɴᴀɴ ᴠɪᴅᴇᴏ {duration} minute(s)"
                )
                is_downloading = False
                return
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception:
        # await pablo.edit(event, f"**Failed To Download** \n**Error :** `{str(e)}`")
        is_downloading = False
        return

    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    YTVID_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("📺 ʏᴏᴜᴛᴜʙᴇ'ᴅᴀ ɪᴢʟᴇ 📺", url=f"{mo}")]])
    capy = f"**🎧️ ᴍᴜᴢɪᴋ ᴠɪᴅᴇᴏ ᴀᴅɪ:** `{thum}` \n\n**👨‍💻️ ᴀɴᴀʜᴛᴀʀ ᴋᴇʟɪᴍᴇɴɪᴢ:** `{urlissed}` \n**😉️ ʏᴏᴜᴛᴜʙᴇ ᴋᴀɴᴀʟɪ:** `{thums}` \n**🔗️ ᴠɪᴅᴇᴏ ʟɪɴᴋ :** `{mo}`"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        reply_markup=YTVID_BUTTONS,
        supports_streaming=True,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ! ʏᴜᴋʟᴜʏᴏʀᴜᴍ` **{urlissed}** `ʏᴏᴜᴛᴜʙᴇ'ᴅᴀɴ!`",
            file_stark,
        ),
    )
    await pablo.delete()
    is_downloading = False
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
