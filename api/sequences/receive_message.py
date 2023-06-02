import logging

from api.bot_messages import create_text_message_list
from api.mecab_function import wakati_text
from api.models import SmartPoll
from api.utils import get_message_text

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
        text1 = "ポールの一覧を表示します"
        text2 = ""
        for item in SmartPoll.objects.all():
            text2.join(item.default_name)
            text2.join("\n")

        result = create_text_message_list(text1, text2)
        return result


def judge_sequence_from_message(event_obj):
    message = get_message_text(event_obj)
    text_result = wakati_text(message)
    logger.info(text_result)
    return 1
