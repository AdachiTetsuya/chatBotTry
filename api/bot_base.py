import json
import logging
import os

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

        requests.post(REPLY_ENDPOINT_URL, data=json.dumps(body), headers=HEADER)

    def get_user_info(self, user_id):
        res = requests.get(USER_INFO_URL + user_id, headers=HEADER)
        text_obj = json.loads(res.text)
        logger.info(text_obj)
        return text_obj
