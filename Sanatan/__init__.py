import logging  
import os
from pyrogram import Client 
from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient
from config import Development as config

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

API_ID = config.API_ID
API_HASH = config.API_HASH
BOT_TOKEN = config.BOT_TOKEN
GROUP_ID = config.GROUP_ID
MONGO_URL = config.MONGO_URL
VIDEO_URL = config.VIDEO_URL 
SUPPORT_CHAT = config.SUPPORT_CHAT 
UPDATE_CHAT = config.UPDATE_CHAT
BOT_USERNAME = config.BOT_USERNAME 
sudo_users = config.sudo_users
OWNER_ID = config.OWNER_ID 

application = Application().build()
Sanatan = Client("Sanatan", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
lol = AsyncIOMotorClient(MONGO_URL)
db = lol['Character_catcher']
collection = db['anime_characters_lol']
user_totals_collection = db['user_totals_lmaoooo']
user_collection = db["user_collection_lmaoooo"]
group_user_totals_collection = db['group_user_totalsssssss']
top_global_groups_collection = db['top_global_groups']
pm_users = db['total_pm_users']
