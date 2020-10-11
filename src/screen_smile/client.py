import json
import base64
import requests
import pyautogui


SERVER_URL = 'http://localhost:5000/smile'


screenshot = pyautogui.screenshot()
screenshot.save('./image.png')
with open('./image.png', 'rb') as img_file:
    payload = {'img': img_file}
    requests.post(SERVER_URL, files=payload)
