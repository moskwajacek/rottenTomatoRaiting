import os
import requests
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env_local_development'
load_dotenv(dotenv_path=env_path)

url = f"https://www.omdbapi.com/demo.aspx/?t=chicago&token={os.getenv('API_TOKEN')}"
headers = {
    'x-api-key': os.getenv('API_KEY')
}

response = requests.request("GET", url, headers=headers).json()

for keyVal in response['Ratings']:
    if (keyVal['Source'] == 'Rotten Tomatoes'):
        print(keyVal['Value'])
