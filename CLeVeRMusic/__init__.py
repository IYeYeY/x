from CLeVeRMusic.core.bot import Zoro
from CLeVeRMusic.core.dir import dirr
from CLeVeRMusic.core.git import git
from CLeVeRMusic.core.userbot import Userbot
from CLeVeRMusic.misc import dbb, heroku

from pyromod import listen  # ← تفعيل pyromod عشان ask تشتغل

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zoro()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

