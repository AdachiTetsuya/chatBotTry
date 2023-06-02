import logging

import MeCab

from api.bot_messages import create_text_message_list
from api.utils import get_message_text

wakati = MeCab.Tagger()

logger = logging.getLogger("api")


def receive_message_function(event_obj):
    """
    テキストメッセージを受け取って、適切な送信メッセージを返す。

    Args:
        event_obj (dict): Messaging API の イベントオブジェクト

    Returns:
        list[dict[str, str]] : reply メソッド用にフォーマットした送信メッセージ
    """

    sequence = judge_sequence_from_message(event_obj)

    if sequence == 1:
        result = create_text_message_list("メッセージ")
        return result


def judge_sequence_from_message(event_obj):
    message = get_message_text(event_obj)
    result = wakati.parse(message)
    logger.info(result)

    return 1
