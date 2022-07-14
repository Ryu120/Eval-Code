# © its-leo-bitch
import logging
from configparser import ConfigParser

from bot.bot import bot
import pyromod.listen
import time

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
    handlers=[
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)


start_time = time.time()

name = 'bot'

"""
API_ID = int(os.environ.get("API_ID", None))
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)
BOTUSERNAME = os.environ.get("BOTUSERNAME", None) 
"""
API_ID = "19733238"
API_HASH = "fe955e75a36ec386ae9ded33061fbd98"
TOKEN = "5566162550:AAFxuB_il3Zfn7fhhRHMZr_CIBRs_aQly2M"
BOTUSERNAME = "RyuEvalBot"

# Extra details
__version__ = '0.0.1'
__author__ = 'pokurt'

# Global Variables
bot = bot(name)
