import os
import argparse
import requests
import json
from rich.console import Console
from config import env_load, API_URL

env_load()
parser = argparse.ArgumentParser()
console = Console()

parser.add_argument(
    "--title", "-t", help="Set film title in quotes to see Rotten Tomatoes rating.")
args = parser.parse_args()

if args.title != None:

    def fetch_data():
        API_KEY = os.getenv('API_KEY')
        url = f"{API_URL}?apikey={API_KEY}&t={args.title}"

        try:
            response = requests.request("GET", url).json()
            if response.get('Ratings'):
                for keyVal in response['Ratings']:
                    if (keyVal['Source'] == 'Rotten Tomatoes'):
                        console.log(
                            f"[red]Rotten Tomatoes for {response['Title']} title is: {keyVal['Value']}[/red]")
            elif response.get('Error'):
                console.log(
                    f"[red]Movie {args.title} title not found.[red]")
            else:
                console.log(
                    f"[red]Raitings error for {args.title} title.[red]")
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    with console.status("[bold green]fatching data...") as status:
        datas = [1]
        while datas:
            console.log(f"[green]Starting feching data.[/green]")
            data = datas.pop(0)
            fetch_data()
            console.log(f"[green]Feching data finished.[/green]")

else:
    console.log("[red]You should pass --title (-t) argument.[/red]")
