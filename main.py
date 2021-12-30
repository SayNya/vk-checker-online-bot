import os
import time

import telegram
import requests
from dotenv import load_dotenv

load_dotenv()

VK_ACCESS_TOKEN = os.getenv('VK_ACCESS_TOKEN')
VK_ID = os.getenv('VK_ID')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    return bot.send_message(CHAT_ID, message)


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': '5.131',
        'access_token': VK_ACCESS_TOKEN,
        'fields': 'online'
    }
    request = requests.post('https://api.vk.com/method/users.get', params=params).json()
    return request['response'][0]['online']


if __name__ == '__main__':
    online = False
    while True:
        status = get_status(VK_ID)
        if not online and status:
            send_message('Online')
            online = True
        elif online and not status:
            send_message('Offline')
            online = False
            print(f'{online=}; {status=}')
        print(f'{online=}; {status=}')
        time.sleep(300)
