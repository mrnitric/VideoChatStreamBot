import asyncio

from pyrogram import filters

from .. import Calls, bot, chat_id
from ..functions import admin_check, user_input, video_stream, youtube_stream

que = asyncio.Queue()
number = 0
loop = asyncio.get_event_loop()


# Stream A Video From Youtube/Telegram


@bot.on_message(
    filters.command(["vplay", "vtelegram"]) & filters.chat(chat_id)
)
async def stream(client, message):
    reply = message.reply_to_message
    user_str = await user_input(message.text)
    if message.command[0][1] == "p" and not user_str:
        return await message.reply(
            "𝙋𝙡𝙚𝙖𝙨𝙚 𝙜𝙞𝙫𝙚 𝙖 𝙮𝙤𝙪𝙩𝙪𝙗𝙚 /link_keyword 𝙤𝙧 𝙧𝙚𝙥𝙡𝙮 /vtelegram 𝙩𝙤 𝙖 𝙫𝙖𝙡𝙞𝙙 𝙫𝙞𝙙𝙚𝙤 𝙩𝙤 𝙨𝙩𝙧𝙚𝙖𝙢 !"
        )
    if message.command[0][1] == "t":
        if not (reply and reply.video):
            return await message.reply(
                "𝙋𝙡𝙚𝙖𝙨𝙚 𝙜𝙞𝙫𝙚 𝙖 𝙮𝙤𝙪𝙩𝙪𝙗𝙚 /link_keyword 𝙤𝙧 𝙧𝙚𝙥𝙡𝙮 /vtelegram 𝙩𝙤 𝙖 𝙫𝙖𝙡𝙞𝙙 𝙫𝙞𝙙𝙚𝙤 𝙩𝙤 𝙨𝙩𝙧𝙚𝙖𝙢 !"
            )
        download_ = await message.reply("𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙏𝙝𝙚 𝙍𝙚𝙥𝙡𝙞𝙚𝙙 𝙑𝙞𝙙𝙚𝙤 ! 𝙃𝙤𝙡𝙙 𝙊𝙣...")
        video = await reply.download(file_name="DOWNLOADS/")
        await download_.delete()
    if Calls.is_running:
        if user_str:
            next_vid = user_str
        else:
            next_vid = video
        await que.put(next_vid)
        global number
        number += 1
        content = user_str if user_str else "𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙑𝙞𝙙𝙚𝙤"
        return await message.reply(
            f"• 𝘼𝙙𝙙𝙚𝙙 **𝙑𝙞𝙙𝙚𝙤🎥** : **__{content}__** 𝙏𝙤 𝙌𝙪𝙚𝙪𝙚 !\n\n**𝙌𝙪𝙚𝙪𝙚𝙙 𝙖𝙩 #{number}**."
        )
    try:
        invideo = user_str if user_str else video
        await video_stream(chat_id, invideo, client, message)
    except Exception as e:
        return await message.reply(e)


# Stop Video Chat


@bot.on_message(filters.command("vstop") & filters.chat(chat_id))
async def stop(client, message):
    if not Calls.is_running:
        return await message.reply("𝙉𝙤 𝙎𝙩𝙧𝙚𝙖𝙢 𝙂𝙤𝙞𝙣𝙜 𝙊𝙣 !")
    global number
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "𝙔𝙤𝙪 𝘿𝙤𝙣𝙩 𝙃𝙖𝙫𝙚 𝙎𝙪𝙛𝙛𝙞𝙘𝙞𝙚𝙣𝙩 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣𝙨 !, 𝙈𝙖𝙠𝙚 𝙎𝙪𝙧𝙚 𝙔𝙤𝙪 𝙃𝙖𝙫𝙚 𝙈𝙖𝙣𝙖𝙜𝙚 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩𝙨"
        )
    await Calls.stop()
    number = 0
    que._queue.clear()
    return await message.reply("𝙏𝙝𝙚 𝙑𝙞𝙙𝙚𝙤 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝙎𝙩𝙤𝙥𝙥𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 !")


# Skip Video Stream


@bot.on_message(filters.command("vskip") & filters.chat(chat_id))
async def skip(client, message):
    global number
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "𝙔𝙤𝙪 𝘿𝙤𝙣𝙩 𝙃𝙖𝙫𝙚 𝙎𝙪𝙛𝙛𝙞𝙘𝙞𝙚𝙣𝙩 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣𝙨 !, 𝙈𝙖𝙠𝙚 𝙎𝙪𝙧𝙚 𝙔𝙤𝙪 𝙃𝙖𝙫𝙚 𝙈𝙖𝙣𝙖𝙜𝙚 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩𝙨"
        )
    if que.empty():
        await message.reply(
            "𝙉𝙤 𝙈𝙤𝙧𝙚 𝙑𝙞𝙙𝙚𝙤𝙨 𝙄𝙣 𝙌𝙪𝙚𝙪𝙚 !\n\n𝙇𝙚𝙖𝙫𝙞𝙣𝙜 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩 ! 𝙭𝘿"
        )
        return await Calls.stop()
    else:
        stuff = await que.get()
        number -= 1
    try:
        await video_stream(chat_id, stuff, client, message)
    except Exception as e:
        return await message.reply(e)


# Playout Ended
@Calls.on_video_playout_ended
async def media_ended(_, __):
    if que.empty():
        await bot.send_message(
            chat_id, "𝙉𝙤 𝙈𝙤𝙧𝙚 𝙑𝙞𝙙𝙚𝙤𝙨 𝙄𝙣 𝙌𝙪𝙚𝙪𝙚 !\n\n𝙇𝙚𝙖𝙫𝙞𝙣𝙜 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩 ! 𝙭𝘿"
        )
        return await Calls.stop()
    else:
        process = await bot.send_message(chat_id, "𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜...")
        stuff = await que.get()
    try:
        if "DOWNLOADS" in stuff:
            thumb, video, title = "./img.jpg", stuff, "𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝘼𝙪𝙙𝙞𝙤"
            await Calls.start_video(video, repeat=False)
        else:
            thumb, video, title = await loop.run_in_executor(
                None, youtube_stream, stuff
            )
        await process.delete()
        await Calls.start_video(video, repeat=False)
        global number
        number -= 1
        ctitle = (await bot.get_chat(chat_id)).title
        return await bot.send_photo(
            chat_id,
            photo=thumb,
            caption=f"𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 !\n\n**• 𝙑𝙞𝙙𝙚𝙤🎥** : **__{title}__**\n**• 𝘾𝙝𝙖𝙩 : {ctitle}**",
        )
    except Exception as e:
        return await bot.send_message(chat_id, e)
