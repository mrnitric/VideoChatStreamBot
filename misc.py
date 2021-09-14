from pyrogram import Client
from pytgcalls import GroupCallFactory as gcf

import config

# Plugins
vsb = dict(root="VideoxD/Handlers")

# Pyro Client
app = Client(
    config.STRING_SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins=vsb,
)
bot = Client(
    "bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=vsb,
)


# pytgcalls

Calls = gcf(app).get_group_call()


# Help Text

HELP = """** 𝙃𝙚𝙧𝙚 𝙞𝙨 𝙖 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙛𝙤𝙧 𝙑𝙞𝙙𝙚𝙤 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝘽𝙤𝙩 **
/vplay - To Stream a Video in Group ( Youtube Search, Youtube Link)
/vtelegram - To Stream a Telegram Video
/vstop - To Stop a Video Stream
/vpause - To Pause a Video Stream
/vresume - To Resume Video Stream
/vskip - To Skip The Current Playing Video
/repo - To Get The Repo
/help , /start - To Get Welcome Menu and Commands (works in private)
/alive - To Check If The Bot Is Alive
• Powered By @Sanki_BOTs •""" 
