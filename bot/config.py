# © its-leo-bitch
import os
import re
from pathlib import Path

class Config:
  API_ID = int(os.environ.get("API_ID", None))
  API_HASH = os.environ.get("API_HASH", None)
  TOKEN = os.environ.get("TOKEN", None)
  BOTUSERNAME = os.environ.get("BOTUSERNAME", None)
