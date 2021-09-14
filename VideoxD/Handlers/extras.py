from pyrogram import filters

from .. import Calls, bot, chat_id
from ..functions import admin_check


@bot.on_message(filters.command("vpause") & filters.chat(chat_id))
async def pause(client, message):
    if not Calls.is_running:
        return await message.reply(
            "𝙏𝙝𝙚𝙧𝙚 𝙞𝙨 𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜, 𝙒𝙝𝙖𝙩 𝙎𝙝𝙖𝙡𝙡 𝙗𝙚 𝙋𝙖𝙪𝙨𝙚𝙙 ?"
        )
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "𝙔𝙤𝙪 𝘿𝙤𝙣𝙩 𝙃𝙖𝙫𝙚 𝙎𝙪𝙛𝙛𝙞𝙘𝙞𝙚𝙣𝙩 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣𝙨 !, 𝙈𝙖𝙠𝙚 𝙎𝙪𝙧𝙚 𝙔𝙤𝙪 𝙃𝙖𝙫𝙚 𝙈𝙖𝙣𝙖𝙜𝙚 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩𝙨"
        )
    if Calls.is_paused:
        return await message.reply(
            "𝙏𝙝𝙚 𝙑𝙞𝙙𝙚𝙤 𝙞𝙨 𝙖𝙡𝙧𝙚𝙖𝙙𝙮 𝙥𝙖𝙪𝙨𝙚𝙙, 𝙒𝙝𝙖𝙩 𝙢𝙤𝙧𝙚 𝙨𝙝𝙖𝙡𝙡 𝙗𝙚 𝙥𝙖𝙪𝙨𝙚𝙙 ?"
        )
    await Calls.set_pause(True)
    return await message.reply("𝙏𝙝𝙚 𝙑𝙞𝙙𝙚𝙤 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝙋𝙖𝙪𝙨𝙚𝙙 ⏸ 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 !")


@bot.on_message(filters.command("vresume") & filters.chat(chat_id))
async def resume(client, message):
    if not Calls.is_running:
        return await message.reply(
            "𝙏𝙝𝙚𝙧𝙚 𝙞𝙨 𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜, 𝙒𝙝𝙖𝙩 𝙎𝙝𝙖𝙡𝙡 𝙗𝙚 𝙍𝙚𝙨𝙪𝙢𝙚𝙙 ?"
        )
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "𝙔𝙤𝙪 𝘿𝙤𝙣𝙩 𝙃𝙖𝙫𝙚 𝙎𝙪𝙛𝙛𝙞𝙘𝙞𝙚𝙣𝙩 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣𝙨 !, 𝙈𝙖𝙠𝙚 𝙎𝙪𝙧𝙚 𝙔𝙤𝙪 𝙃𝙖𝙫𝙚 𝙈𝙖𝙣𝙖𝙜𝙚 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩𝙨"
        )
    if not Calls.is_paused:
        return await message.reply(
            "𝙏𝙝𝙚 𝙑𝙞𝙙𝙚𝙤 𝙞𝙨 𝙖𝙡𝙧𝙚𝙖𝙙𝙮 𝙥𝙡𝙖𝙮𝙞𝙣𝙜, 𝙒𝙝𝙖𝙩 𝙢𝙤𝙧𝙚 𝙨𝙝𝙖𝙡𝙡 𝙗𝙚 𝙧𝙚𝙨𝙪𝙢𝙚𝙙 ?"
        )
    await Calls.set_pause(False)
    return await message.reply("𝙏𝙝𝙚 𝙑𝙞𝙙𝙚𝙤 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝙍𝙚𝙨𝙪𝙢𝙚𝙙 ▶️ 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 !")
