import requests
import time

API_URL = "https://api.telegram.org/bot"
TOKEN = "7708458048:AAFgnRq2j6P0Eu8SX5TcFhrxNwvC-efuo5E"
TEXT = "some text"
MAX_COUNTER = 1000

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print(f"{TEXT}{counter}")

    updates = requests.get(f"{API_URL}{TOKEN}/getUpdates?offset={offset + 1}").json()
    print(offset)

    if updates["result"]:
        for result in updates["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]
            requests.get(f"{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}{counter}")

    time.sleep(1)
    counter += 1




