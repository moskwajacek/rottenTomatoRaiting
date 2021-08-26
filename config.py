import os
from pathlib import Path
from dotenv import load_dotenv

API_URL = "http://www.omdbapi.com"


def env_load():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
