import logging

from api.bot_messages import create_text_message_list
from api.data.operation import OPERATION_DATA, SKY_PHOTO
from api.data.target import TARGET_VALUE_DATA
from api.mecab_function import wakati_text
from api.models import SmartPoll, UserPollRelation
from api.utils import get_message_text, get_user_line_id

logger = logging.getLogger("api")


def receive_message_function(event_obj):
    """
    テキストメッセージを受け取って、適切な送信メッセージを返す。

    Args:
        event_obj (dict): Messaging API の イベントオブジェクト

    Returns:
        list[dict[str, str]] : reply メソッド用にフォーマットした送信メッセージ
    """

    line_id = get_user_line_id(event_obj)

    sequence = judge_sequence_from_message(event_obj)

    if sequence["target"] and sequence["operation"]:
        if sequence["operation"] == "sky_photo":
            if smart_poll := SmartPoll.objects.filter(can_sky_photo=True).first():
                url = smart_poll.get_sky_photo()
                result = {
                    "type": "image",
                    "originalContentUrl": url,
                    "previewImageUrl": url,
                }
                return result

        if sequence["operation"] == "list":
            if sequence["target"] == "smart_polls":
                text1 = "ポールの一覧を表示します"
                name_list = [
                    item.poll_name
                    for item in UserPollRelation.objects.filter(user__line_id=line_id)
                ]
                text2 = "\n".join(name_list)

                result = create_text_message_list(text1, text2)
                return result

    result = create_text_message_list("わからない")
    return result


def judge_sequence_from_message(event_obj):
    message = get_message_text(event_obj)
    text_result = wakati_text(message)

    operation = ""
    target = ""
    post_data = ""

    for k, v_list in OPERATION_DATA.items():
        for v in v_list:
            if v in text_result:
                operation = k
                break
        else:
            continue
        break

    for v in SKY_PHOTO:
        if v in text_result:
            operation = "sky_photo"
            break

    for k, v_list in TARGET_VALUE_DATA.items():
        for v in v_list:
            if v in text_result:
                target = k
                break
        else:
            continue
        break

    result = {"operation": operation, "target": target, "post_data": post_data}

    return result
