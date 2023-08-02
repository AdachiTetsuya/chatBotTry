import logging

from api.bot_messages import create_text_message_list
from api.chatter_bot_func import get_chatterbot_message
from api.models import CustomUser, UserPollRelation
from api.sequences.about_buddy import (
    register_MB,
    register_primary,
    remove_MB,
    remove_primary,
    show_MB_list,
    show_MB_operation_list,
)
from api.sequences.change_property import (
    new_age_input_prompt,
    new_gender_input_prompt,
    new_name_input_prompt,
    show_all_property,
    show_change_prop_list,
    show_change_prop_obj_list,
)
from api.sequences.etc_func import (
    quick_replay_no,
    show_people_level,
    show_temperature,
    show_weather_detail,
    sky_photo,
)
from api.sequences.judge_sequence import judge_sequence_from_message
from api.sequences.response_message import everyone_response, single_response

logger = logging.getLogger("api")


def receive_message_function(event_obj, user: CustomUser, user_poll_relations: UserPollRelation):
    """
    テキストメッセージを受け取って、適切な送信メッセージを返す。

    Args:
        event_obj (dict): Messaging API の イベントオブジェクト
        user (CustomUser): CustomUser インスタンス
        user_poll_relations (UserPollRelation): UserPollRelation インスタンス

    Returns:
        list[dict[str, str]] : reply メソッド用にフォーマットした送信メッセージ
    """

    sequence = judge_sequence_from_message(event_obj, user_poll_relations, user)
    logger.info(sequence)

    if operation := sequence["operation"]:
        if operation == "sky_photo":
            return sky_photo()
        elif operation == "show_temperature":
            return show_temperature()
        elif operation == "show_weather_detail":
            return show_weather_detail()
        elif operation == "show_people_level":
            return show_people_level()

        elif operation == "everyone_response":
            return everyone_response(user_poll_relations)
        elif operation == "single_response":
            return single_response(sequence["target"])

        elif operation == "show_MB_list":
            return show_MB_list(user_poll_relations)
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

        elif operation == "show_all_property":
            return show_all_property(user_poll_relations, user)
        elif operation == "show_change_prop_obj_list":
            return show_change_prop_obj_list(user_poll_relations)
        elif operation == "show_change_prop_list":
            return show_change_prop_list(sequence["target"])

        elif operation == "new_name_input_prompt":
            return new_name_input_prompt(sequence["target"], user)
        elif operation == "new_age_input_prompt":
            return new_age_input_prompt(sequence["target"], user)
        elif operation == "new_gender_input_prompt":
            return new_gender_input_prompt(sequence["target"], user)

        elif operation == "quick_replay_no":
            return quick_replay_no()

    not_ope_replay = get_chatterbot_message(event_obj)

    result = create_text_message_list(not_ope_replay)
    return result
