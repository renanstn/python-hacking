import os
import requests
import pyautogui


SERVER_URL = 'http://localhost:5000/smile'


screenshot = pyautogui.screenshot()
screenshot.save('./tmp.png')
with open('./tmp.png', 'rb') as img_file:
    payload = {'img': img_file}
    requests.post(SERVER_URL, files=payload)
os.remove('tmp.png')
