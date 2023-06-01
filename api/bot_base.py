import os

import urllib.request
import json

REPLY_ENDPOINT_URL = os.getenv("REPLY_ENDPOINT_URL", "")
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN", "")

HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + LINE_ACCESS_TOKEN
}

class LineBotMSG():
    def __init__(self) -> None:
        pass
    
    def reply(self, reply_token, messages):
        body = {
            'replyToken': reply_token,
            'messages': messages
        }
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)