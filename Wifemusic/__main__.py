import asyncio
import importlib
import logging

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Wifemusic import app, userbot
from Wifemusic.core.call import Anony
from Wifemusic.misc import sudo
from Wifemusic.Modules import *
from Wifemusic.utils.database import get_banned_users, get_gbanned

locks = {}
last_user = {}
warned_users = {}
message_counts = {}
sent_characters = {}
last_characters = {}
first_correct_guesses = {}

BANNED_USERS = config.BANNED_USERS  # Assuming this is defined in config.py

LOGGER = logging.getLogger(__name__)

async def init():
    if not all(getattr(config, f"STRING{i+1}", None) for i in range(5)):
        LOGGER.error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()

    try:
        users = await get_gbanned()
        BANNED_USERS.update(users)

        users = await get_banned_users()
        BANNED_USERS.update(users)
    except Exception as e:
        LOGGER.error(f"Error while retrieving banned users: {e}")

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module("Wifemusic.Modules." + all_module)

    LOGGER.info("Successfully Imported Modules...")

    await userbot.start()
    await Anony.start()

    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER.error("Please turn on the video chat of your log group/channel.\n\nStopping Bot...")
        exit()
    except Exception as e:
        LOGGER.error(f"Error while starting stream call: {e}")

    await Anony.decorators()

    LOGGER.info("Bot started successfully.")

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER.info("Stopping WAIFU Music Bot...")

async def message_counter(update, context):
    # Your message counter functionality here
    pass

async def send_image(update, context):
    # Your send image functionality here
    pass

async def guess(update, context):
    # Your guess functionality here
    pass

async def fav(update, context):
    # Your favorite functionality here
    pass

def main():
    """Run bot."""
    application.add_handler(CommandHandler(["guess", "protecc", "collect", "grab", "hunt"], guess, run_async=True))
    application.add_handler(CommandHandler("fav", fav, run_async=True))
    application.add_handler(MessageHandler(Filters.all, message_counter, run_async=True))

    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    main()
