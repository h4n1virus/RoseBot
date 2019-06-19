import logging
import os
import sys
from datetime import datetime

import dotenv
from pyrogram import Client


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("pyrogram").setLevel(logging.WARN)
LOGS = logging.getLogger(__name__)


# Check for Python 3.6 or newer
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGS.error("You MUST use at least Python 3.6. Bot Quitting")
    quit(1)


dotenv.load_dotenv()


# APIS
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CC_API = os.getenv("CC_API")
THECATAPI = os.getenv("THECATAPI")
DETECTLANGUAGEAPI = os.getenv("DETECTLANGUAGEAPI")
OCRAPIKEY = os.getenv("OCRAPIKEY")
VIRUSTOTALAPIKEY = os.getenv("VIRUSTOTALAPIKEY")
OMDBAPIKEY = os.getenv("OMDBAPIKEY")


# FILEIDS
FILEIDS_DIR = os.getenv("FILEIDS_DIR")


BOT = Client(session_name="RoseBot", api_id=API_ID, api_hash=API_HASH)