import logging

from api.bot_messages import create_text_message_list
from api.data.operation import OPERATION_DATA, PERSONAL_OPERATION_DATA
from api.mecab_function import wakati_text
from api.models import CustomUser, UserPollRelation
from api.sequences.about_buddy import (
    register_MB,
    register_primary,
    remove_MB,
    remove_primary,
    show_MB_operation_list,
)
from api.sequences.change_property import (
    new_name_input_prompt,
    show_change_prop_list,
    show_change_prop_obj_list,
)
from api.sequences.etc_func import show_temperature, sky_photo
from api.sequences.response_message import everyone_response, single_response
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
    user = CustomUser.objects.get(line_id=line_id)
    user_poll_relations = UserPollRelation.objects.filter(user=user)

    sequence = judge_sequence_from_message(event_obj, user_poll_relations, user)

    if operation := sequence["operation"]:
        if operation == "sky_photo":
            return sky_photo()

        elif operation == "show_temperature":
            return show_temperature()

        elif operation == "everyone_response":
            return everyone_response(user_poll_relations)

        elif operation == "single_response":
            return single_response(sequence["target"])

        elif operation == "show_MB_operation_list":
            return show_MB_operation_list(user_poll_relations)

        elif operation == "register_MB":
            return register_MB(sequence["target"])

        elif operation == "remove_MB":
            return remove_MB(sequence["target"])

        elif operation == "register_primary":
            return register_primary(sequence["target"], user_poll_relations)

        elif operation == "remove_primary":
            return remove_primary(sequence["target"], user_poll_relations)

        elif operation == "show_change_prop_obj_list":
            return show_change_prop_obj_list(user_poll_relations)

        elif operation == "show_change_prop_list":
            return show_change_prop_list(sequence["target"])

        elif operation == "new_name_input_prompt":
            return new_name_input_prompt(user)

    result = create_text_message_list("わからない")
    return result


def judge_sequence_from_message(event_obj, user_poll_relations, user):
    message = get_message_text(event_obj)
    text_result = wakati_text(message)

    poll_name_list = [item.poll_name for item in user_poll_relations]

    result = {"operation": "", "target": ""}

    # 名前が入ってる場合の処理
    for i, poll_name in enumerate(poll_name_list):
        if poll_name not in text_result:
            continue

        for k, v_list in PERSONAL_OPERATION_DATA.items():
            if type(v_list[0]) is str:
                for v in v_list:
                    if v in text_result:
                        result["operation"] = k
                        result["target"] = user_poll_relations[i]
                        return result
            else:
                if set(v_list[0]).issubset(text_result):
                    result["operation"] = k
                    result["target"] = user_poll_relations[i]
                    return result

        result["operation"] = "single_response"
        result["target"] = user_poll_relations[i]

    # 「私」という言葉が入ってる場合の処理
    if "私" in text_result:
        for k, v_list in PERSONAL_OPERATION_DATA.items():
            if set(v_list[0]).issubset(text_result):
                result["operation"] = k
                result["target"] = user
                return result

    for k, v_list in OPERATION_DATA.items():
        if type(v_list[0]) is str:
            for v in v_list:
                if v in text_result:
                    result["operation"] = k
                    return result
        else:
            if set(v_list[0]).issubset(text_result):
                result["operation"] = k
                return result

    return result
