from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import HELP, bot

# basic commands


@bot.on_message(filters.command("alive"))
async def startxd(client, message):
    return await message.reply("𝙔𝙚𝙨 𝙄 𝙖𝙢 𝘼𝙡𝙞𝙫𝙚 !,𝙒𝙝𝙤 𝘾𝙖𝙧𝙚𝙨 𝘼𝙗𝙤𝙪𝙩 𝙎𝙤𝙢𝙚𝙤𝙣𝙚 𝙀𝙡𝙨𝙚 !")


@bot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(client, message):
    sender_mention = message.from_user.mention
    return await message.reply(
        f"𝙃𝙚𝙮 👀 ! {sender_mention}, 𝙏𝙝𝙞𝙨 𝙞𝙨 𝙖 𝙫𝙞𝙙𝙚𝙤 𝙨𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝙗𝙤𝙩. 𝙃𝙚𝙧𝙚 𝙞𝙨 𝙖 𝙡𝙞𝙣𝙠 𝙩𝙤 𝙢𝙮 𝙨𝙤𝙪𝙧𝙘𝙚 𝙘𝙤𝙙𝙚 !",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="- 𝙍𝙚𝙥𝙤𝙨𝙞𝙩𝙤𝙧𝙮 -",
                        url="https://github.com/mrnitric/VideoChatStreamBot",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="- 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 -", callback_data="commands"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="- 𝙊𝙬𝙣𝙚𝙧 -",
                        url="https://t.me/iTs_Nitric",
                    )
                ],
            ]
        ),
    )


@bot.on_callback_query(filters.regex("commands"))
async def command_(_, cb):
    await bot.send_message(cb.message.chat.id, text=HELP)
    return await cb.message.delete()
