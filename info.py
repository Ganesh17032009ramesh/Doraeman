#Here is the updated `info.py` with the changes you requested for your Doraemon project:

```python
import re 
from os import getenv, environ
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO
)

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 20902603
API_HASH = "79e5caa103a9e9fb0183390b4800845d"
BOT_TOKEN = "7719610759:AAEiFaJr55YUMpAwedrWglcU1BXpQZFX_-Q"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = True
PICS = (environ.get('PICS', 'https://envs.sh/Rxj.jpg https://envs.sh/Rxc.jpg https://envs.sh/RxZ.jpg https://envs.sh/Rx5.jpg')).split()
PRIME_LOGO = "https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg"

# Admins, Channels & Users
ADMINS = [6283322330]
CHANNELS = [-1002282731258]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '6283322330').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = "mongodb+srv://Mastersender:17032008@cluster0.dt8i8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = 'Telegram_files'

# LOG CHANNELS
LOG_CHANNEL = -1002263199167
LAZY_GROUP_LOGS = 0
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', LOG_CHANNEL))
PRIME_MEMBERS_LOGS = 0

# Premium Access
PRIME_USERS = [6283322330]
LAZY_RENAMERS = ADMINS
LZURL_PRIME_USERS = [6283322330]

QR_CODE_IMG = "https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg"
UPI_ID = "lazydeveloper@ybl"

# Other settings
TUTORIAL = "https://t.me/real_MoviesAdda3/186"
IS_TUTORIAL = True
SUPPORT_CHAT = "https://t.me/+5BjSl3U6r2VkOWI9"
P_TTI_SHOW_OFF = False
IMDB = True
SINGLE_BUTTON = False
CUSTOM_FILE_CAPTION = "⚡<b>File uploaded by [Doraemon](https://t.me/jeevanmovieschannel)</b>⚡\n\n📂<b>File Name:</b> ⪧ {file_caption} \n <b>Size: </b>{file_size}\n\n❤"
BATCH_FILE_CAPTION = CUSTOM_FILE_CAPTION
IMDB_TEMPLATE = "<b>Your Query: {query}</b> \n‌‌‌‌🎁Support: @Cr3atives_Cortex 🎁\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately"
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MAX_LIST_ELM = None
INDEX_REQ_CHANNEL = LOG_CHANNEL
FILE_STORE_CHANNEL = [-1002315728390]

MELCOW_NEW_USERS = True
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = False

# LazyRenamer Configs
FLOOD = 10
LAZY_MODE = False

# Requested Content Template variables
ADMIN_USRNM = "Cr3atives_Cortex"
MAIN_CHANNEL_USRNM = "jeevanmovieschannel"
DEV_CHANNEL_USRNM = "Cr3atives_Cortex"
LAZY_YT_HANDLE = "Cr3atives_Cortex"
MOVIE_GROUP_USERNAME = "https://t.me/+1V8COnltCGs5OWY1"

# URL Shortner
URL_MODE = False
URL_SHORTENR_WEBSITE = "atglinks.com"
URL_SHORTNER_WEBSITE_API = "72a7f0131e5e657e37cf7e2a9e928a616b671cf5"

# Online Stream and Download
PORT = 8080
NO_PORT = False
APP_NAME = None
ON_HEROKU = False
BIND_ADRESS = "0.0.0.0"
FQDN = "doraemonapp.herokuapp.com"
URL = "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = 60
WORKERS = 4
SESSION_NAME = "LazyBot"
MULTI_CLIENT = False
name = "LazyPrincess"
PING_INTERVAL = 1200

# Download Tutorial Button
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/real_MoviesAdda3"

# Custom Caption Under Button
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/real_MoviesAdda3"

# Log details
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template.\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

# Credit
LOG_STR += "\nCredit @LazyDeveloper.\nPlease Don't remove credit. Born to make history @LazyDeveloper!\nThank you LazyDeveloper for helping us in this Journey\n🥰 Thank you for giving me credit @LazyDeveloperr 🥰"
```

This final `info.py` incorporates all your changes, including the required variables and settings. Let me know if anything else needs to be adjusted!
