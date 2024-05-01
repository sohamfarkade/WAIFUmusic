from waifumusic.core.bot import waifu
from waifumusic.core.dir import dirr
from waifumusic.core.git import git
from waifumusic.core.userbot import Userbot
from waifumusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = waifu()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
