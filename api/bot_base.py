import json
import logging
import os
import urllib.request

import requests

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
USER_INFO_URL = "https://api.line.me/v2/bot/profile/"
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN", "")

HEADER = {"content-Type": "application/json", "Authorization": "Bearer " + LINE_ACCESS_TOKEN}

logger = logging.getLogger("api")


class LineBotMSG:
    def __init__(self) -> None:
        pass

    def reply(self, reply_token, messages):
        body = {"replyToken": reply_token, "messages": messages}

        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        with urllib.request.urlopen(req) as res:
            body = res.read()

    def get_user_info(self, user_id):
        res = requests.get(USER_INFO_URL + user_id, headers=HEADER)
        text_obj = json.loads(res.text)
        logger.info(text_obj)
        return text_obj
