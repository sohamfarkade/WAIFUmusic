from Wifemusic.core.bot import Anony
from Wifemusic.core.dir import dirr
from Wifemusic.core.git import git
from Wifemusic.core.userbot import Userbot
from Wifemusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
import logging  
import os
from pyrogram import Client 
from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)



API_ID= .API_ID
API_HASH= .API_HASH
BOT_TOKEN = .BOT_TOKEN
GROUP_ID = .GROUP_ID
MONGO_DB_URI= .MONGO_DB_URI
VIDEO_URL = .VIDEO_URL 
SUPPORT_CHAT = .SUPPORT_CHAT 
UPDATE_CHAT = .UPDATE_CHAT
BOT_USERNAME = .BOT_USERNAME 
OWNER_ID = .OWNER_ID 

application = Application.builder().token(TOKEN).build()
Wifemusic = Client("wifemusic", API_ID, API_HASH, bot_token=BOT_TOKEN)
lol = AsyncIOMotorClient(MONGO_DB_URI)
MONGO_DB_URI = lol['Character_catcher']
collection = MONGO_DB_URI['anime_characters_lol']
user_totals_collection = MONGO_DB_URI['user_totals_lmaoooo']
user_collection = MONGO_DB_URI["user_collection_lmaoooo"]
group_user_totals_collection = MONGO_DB_URI['group_user_totalsssssss']
top_global_groups_collection = MONGO_DB_URI['top_global_groups']
pm_users = MONGO_DB_URI['total_pm_users']
