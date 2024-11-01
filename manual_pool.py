import requests
import time
import os

API_URL = "https://api.telegram.org/bot"
TOKEN = os.getenv("EMPTY_TOKEN")
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




