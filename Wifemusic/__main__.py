import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters

import config
from Wifemusic import collection, top_global_groups_collection, group_user_totals_collection, user_collection, user_totals_collection, Wifemusic, application, SUPPORT_CHAT, SUPPORT_CHANNEL, db, LOGGER
from Wifemusic.Modules import ALL_MODULES

from Wifemusic import app as music_app, userbot
from Wifemusic.core.call import Anony
from Wifemusic.utils.database import get_banned_users, get_gbanned

locks = {}
message_counters = {}
spam_counters = {}
last_characters = {}
sent_characters = {}
first_correct_guesses = {}
message_counts = {}

BANNED_USERS = set()

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await Wifemusic.start()
    await music_app.start()

    for module_name in ALL_MODULES:
        imported_module = importlib.import_module("Wifemusic.Modules." + module_name)
        importlib.import_module("Wifemusic.Modules" + module_name)

    LOGGER("Wifemusic.Modules").info("Successfully Imported Modules...")

    await userbot.start()
    await Anony.start()

    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Wifemusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await Anony.decorators()
    LOGGER("Wifemusic").info(
        "\x41\x6e\x6f\x6e\x58\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\n\n\x44\x6f\x6e'\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x46\x61\x6c\x6c\x65\x6e\x41\x73\x73\x6f\x63\x69\x61\x74\x69\x6f\x6e"
    )

    application.add_handler(CommandHandler(["guess", "protecc", "collect", "grab", "hunt"], guess, block=False))
    application.add_handler(CommandHandler("fav", fav, block=False))
    application.add_handler(MessageHandler(Filters.ALL, message_counter, block=False))

    await idle()

    await Wifemusic.stop()
    await music_app.stop()
    await userbot.stop()

    LOGGER("Wifemusic").info("Stopping WAIFU Music Bot...")

async def message_counter(update: Update, context: CallbackContext) -> None:
    # Message counter logic from Sanatan
    pass

async def guess(update: Update, context: CallbackContext) -> None:
    # Guess logic from Sanatan
    pass

async def fav(update: Update, context: CallbackContext) -> None:
    # Fav logic from Sanatan
    pass

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
