import os
import re
import logging
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Regex to validate IDs
id_pattern = re.compile(r'^-?\d+$')


# Utility to load and validate environment variables
def get_env_var(key, default=None, required=False, value_type=str):
    """Fetch an environment variable, validate and cast its type."""
    value = os.getenv(key, default)
    if required and value is None:
        raise ValueError(f"Environment variable {key} is required but not set.")
    if value_type == int:
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"Environment variable {key} must be an integer.")
    return value


# Function to validate URLs
def is_valid_url(url):
    return url.startswith(("http://", "https://"))


# Telegram Bot Configuration
API_ID = 20902603  # Replace with your actual API_ID if needed
API_HASH = '79e5caa103a9e9fb0183390b4800845d'
BOT_TOKEN = '8001090344:AAHQIgA76UDN5bNKWtuLY0DlLnBlYWRzZms'

# Bot Sessions
SESSION = 'Media_search'

# Admins and Channels
ADMINS = [6283322330]  # Admin Telegram ID(s)
CHANNELS = [-1002282731258]  # Channel ID(s)

# Database Config
DATABASE_URI = 'mongodb+srv://Mastersender:17032008@cluster0.dt8i8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
DATABASE_NAME = 'cluster0'
COLLECTION_NAME = 'Telegram_files'

# Logging Channels
LOG_CHANNEL = -1002374637289  # Log channel ID
BIN_CHANNEL = 0  # Default to 0 if not provided

# Misc Configurations
START_IMG = [
    'https://envs.sh/Yva.jpg'  # Updated to your new image URL
]
FORCESUB_IMG = 'https://example.com/forcesub.jpg'  # Replace with your image URL

# Bot Features
SPELL_CHECK = True  # Enable or disable spell check
AUTO_FILTER = True  # Enable or disable auto filter
IMDB = True  # IMDB feature is now enabled

# Language and Quality Lists
LANGUAGES = [
    "Tamil", "Tam", "Telugu", "Tel", "Kannada", "kan", 
    "Malayalam", "Mal", "Hindi", "Hin", "English", "Eng",
    "Korean", "Kor", "Japanese", "Jap", "Chinese", "Chi",
    "Dual", "Multi"
]
QUALITIES = [
    "HdRip", "web-dl", "bluray", "hdr", "fhd", "240p",
    "360p", "480p", "540p", "720p", "960p", "1080p",
    "1440p", "2K", "2160p", "4k", "5K", "8K"
]
YEARS = [str(i) for i in range(2024, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

# Logging success
logger.info("info.py loaded successfully with all configurations!")

