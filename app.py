import os
import argparse
import requests
from config import env_load, API_URL

env_load()
parser = argparse.ArgumentParser()

parser.add_argument(
    "--title", "-t", help="Set film title in quotes to see Rotten Tomatoes rating.")
args = parser.parse_args()

if args.title != None:

    API_KEY = os.getenv('API_KEY')
    url = f"{API_URL}?apikey={API_KEY}&t={args.title}"

    response = requests.request("GET", url).json()

    if len(response['Ratings']) > 0:
        for keyVal in response['Ratings']:
            if (keyVal['Source'] == 'Rotten Tomatoes'):
                print(
                    f"Rotten Tomatoes for {response['Title']} title is: {keyVal['Value']}")
    else:
        print(f"No raitings avealible for {args.title} title.")
else:
    print("You should pass --title (-t) argument.")
