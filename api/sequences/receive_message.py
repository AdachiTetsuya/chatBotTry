import logging

from api.bot_messages import create_text_message_list
from api.data.operation import OPERATION_DATA
from api.data.target import TARGET_VALUE_DATA
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

    if sequence["target"] & sequence["operation"]:
        if sequence["target"] == "smart_polls":
            if sequence["operation"] == "list":
                text1 = "ポールの一覧を表示します"
                name_list = [item.default_name for item in SmartPoll.objects.all()]
                text2 = "\n".join(name_list)

                result = create_text_message_list(text1, text2)
                return result

    result = create_text_message_list("わからない")
    return result


def judge_sequence_from_message(event_obj):
    message = get_message_text(event_obj)
    text_result = wakati_text(message)

    target = ""
    operation = ""

    for k, v_list in TARGET_VALUE_DATA.items():
        for v in v_list:
            if v in text_result:
                target = k
                break
        else:
            continue
        break

    for k, v_list in OPERATION_DATA.items():
        for v in v_list:
            if v in text_result:
                operation = k
                break
        else:
            continue
        break

    result = {"target": target, "operation": operation}

    return result
