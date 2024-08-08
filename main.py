import requests
import json
import schedule
import time

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

def send_discord_message(msg: str, channel_id: str):
    headers = {
        'Authorization': f'Bot {TOKEN}',
        'Content-Type': 'application/json',
    }
    message = json.dumps({'content': msg})

    req = requests.post(f'https://discordapp.com/api/channels/{channel_id}/messages', headers=headers, data=message)

# send_discord_message('hello world', '1129419871046865031')

schedule.every().day.at("6:00").do(send_discord_message, 'Good morning', '1129419871046865031')

while True:
    schedule.run_pending()
    time.sleep(5)