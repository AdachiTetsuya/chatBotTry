import json
import os

import requests

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
USER_INFO_URL = "https://api.line.me/v2/bot/profile/"
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN", "")

HEADER = {"content-Type": "application/json", "Authorization": "Bearer " + LINE_ACCESS_TOKEN}


class LineBotMSG:
    """Line API インターフェース

    Line API を叩く用のメソッドを提供する
    """

    def __init__(self) -> None:
        pass

    def reply(self, reply_token, messages):
        """返信用メソッド

        LINE の 返信用の API を叩く

        Args:
            reply_token (str): 返信用のトークン
            messages (list[dict[str, str]]): 返信するメッセージ内容
        """

        body = {"replyToken": reply_token, "messages": messages}

        requests.post(REPLY_ENDPOINT_URL, data=json.dumps(body), headers=HEADER)

    def get_user_info(self, user_id):
        """ユーザ情報の取得用メソッド

        LINE の ユーザ情報の取得用の API を叩く

        Args:
            user_id (str): Line で一意なユーザID

        Returns:
            dict[str, str]: ユーザ情報が格納された辞書
        """
        res = requests.get(USER_INFO_URL + user_id, headers=HEADER)
        text_obj = json.loads(res.text)
        return text_obj
