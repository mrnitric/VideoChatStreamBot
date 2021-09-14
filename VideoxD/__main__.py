import asyncio

from misc import Calls, app, bot
from pyrogram import idle


async def init():
    await app.start()
    print("𝙐𝙨𝙚𝙧 𝙖𝙘𝙘𝙤𝙪𝙣𝙩 𝙄𝙣𝙞𝙩𝙞𝙖𝙡𝙞𝙯𝙚𝙙.")
    await bot.start()
    print("𝘽𝙤𝙩 𝙄𝙣𝙞𝙩𝙞𝙖𝙡𝙞𝙯𝙚𝙙.")
    print(
        "𝙔𝙤𝙪 𝙈𝙞𝙜𝙝𝙩 𝙨𝙚𝙚 𝙉𝙤 𝙋𝙡𝙪𝙜𝙞𝙣𝙨 𝙇𝙤𝙖𝙙𝙚𝙙 𝙏𝙝𝙖𝙩𝙨 𝘼 𝘽𝙪𝙜 𝘽𝙮 𝙡𝙖𝙩𝙚𝙨𝙩 𝙫𝙚𝙧𝙨𝙞𝙤𝙣 𝙤𝙛 𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢, 𝙋𝙡𝙪𝙜𝙞𝙣𝙨 𝙝𝙖𝙫𝙚 𝘽𝙚𝙚𝙣 𝙇𝙤𝙖𝙙𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮."
    )
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(init())
