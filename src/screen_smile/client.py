import os
import time
import requests
import pyautogui


SERVER_URL = 'http://localhost:5000/smile'
TIMER = 60


while True:
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save('./tmp.png')
        with open('./tmp.png', 'rb') as img_file:
            payload = {'img': img_file}
            requests.post(SERVER_URL, files=payload)
        os.remove('tmp.png')
        time.sleep(TIMER)
    except requests.exceptions.ConnectionError:
        pass
