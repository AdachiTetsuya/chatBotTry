import json
import os

import requests

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
USER_INFO_URL = "https://api.line.me/v2/bot/profile/"

PUSH_MESSAGE_URL = "https://api.line.me/v2/bot/message/push"
MULTI_CAST_MESSAGE_URL = "https://api.line.me/v2/bot/message/multicast"
BROAD_CAST_MESSAGE_URL = "https://api.line.me/v2/bot/message/broadcast"

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

    def push_message(self, user_line_id, messages):
        """プッシュメッセージ送信用メソッド

        LINE の プッシュメッセージ送信用の API を叩く

        Args:
            user_line_id (str): 送信先のユーザのラインID
            messages (list[dict[str, str]]): 返信するメッセージ内容
        """
        body = {"to": user_line_id, "messages": messages}
        requests.post(PUSH_MESSAGE_URL, data=json.dumps(body), headers=HEADER)

    def multi_cast_message(self, user_line_ids, messages):
        """マルチキャストメッセージ送信用メソッド

        LINE の マルチキャストメッセージ送信用の API を叩く

        Args:
            user_line_ids (list(str)): 送信先の複数のユーザのラインID
            messages (list[dict[str, str]]): 返信するメッセージ内容
        """
        body = {"to": user_line_ids, "messages": messages}
        requests.post(MULTI_CAST_MESSAGE_URL, data=json.dumps(body), headers=HEADER)

    def broad_cast_message(self, messages):
        """ブロードキャストメッセージ送信用メソッド

        LINE の ブロードキャストメッセージ送信用の API を叩く

        Args:
            messages (list[dict[str, str]]): 返信するメッセージ内容
        """
        body = {"messages": messages}
        requests.post(BROAD_CAST_MESSAGE_URL, data=json.dumps(body), headers=HEADER)
