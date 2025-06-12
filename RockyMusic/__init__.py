from RockyMusic.core.bot import Rocky
from RockyMusic.core.dir import dirr
from RockyMusic.core.git import git
from RockyMusic.core.userbot import Userbot
from RockyMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
