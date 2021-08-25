import os
import argparse
import requests
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env_local_development'
load_dotenv(dotenv_path=env_path)
parser = argparse.ArgumentParser()

parser.add_argument(
    "--title", "-t", help="Set film title in quotes to see Rotten Tomatoes rating.")
args = parser.parse_args()

if args.title != None:

    api_key = os.getenv('API_KEY')
    url = f"http://www.omdbapi.com?apikey={api_key}&t={args.title}"
    response = requests.request("GET", url).json()

    if len(response['Ratings']) < 0:
        for keyVal in response['Ratings']:
            if (keyVal['Source'] == 'Rotten Tomatoes'):
                print("Rotten Tomatoes for film title is: %s" %
                      keyVal['Value'])
    else:
        print('No raitings avealible for title.')
else:
    print("You should pass --title (-t) argument.")
