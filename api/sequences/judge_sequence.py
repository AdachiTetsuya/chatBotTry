import logging

from api.about_comment_count import update_comment_count_and_relationship_level
from api.data.operation import OPERATION_DATA, PERSONAL_OPERATION_DATA
from api.mecab_function import wakati_text
from api.models import UserPollRelation
from api.utils import get_message_text

logger = logging.getLogger("api")


def judge_poll_name_contain(message, user_poll_relations: list[UserPollRelation]):
    poll_name_list = [item.poll_name for item in user_poll_relations]
    for i, poll_name in enumerate(poll_name_list):
        if poll_name in message:
            return user_poll_relations[i]


def judge_sequence_from_message(event_obj, user_poll_relations, user):
    message = get_message_text(event_obj)
    target_poll = judge_poll_name_contain(message, user_poll_relations)

    separated_text_list = wakati_text(message)
    logger.info(separated_text_list)

    result = {"operation": "", "target": ""}

    # ポールの名前が入ってる場合の処理
    if target_poll:
        update_comment_count_and_relationship_level(target_poll)

        for op_name, op_word_list in PERSONAL_OPERATION_DATA.items():
            if type(op_word_list[0]) is str:
                for op_word in op_word_list:
                    if op_word in separated_text_list:
                        result["operation"] = op_name
                        result["target"] = target_poll
                        return result
            else:
                if set(op_word_list[0]).issubset(separated_text_list):
                    result["operation"] = op_name
                    result["target"] = target_poll
                    return result

        result["operation"] = "single_response"
        result["target"] = target_poll

    # 「私」という言葉が入ってる場合の処理
    if "私" in separated_text_list:
        for op_name, op_word_list in PERSONAL_OPERATION_DATA.items():
            if set(op_word_list[0]).issubset(separated_text_list):
                result["operation"] = op_name
                result["target"] = user
                return result

    for op_name, op_word_list in OPERATION_DATA.items():
        if type(op_word_list[0]) is str:
            for op_word in op_word_list:
                if op_word in separated_text_list:
                    result["operation"] = op_name
                    return result
        else:
            if set(op_word_list[0]).issubset(separated_text_list):
                result["operation"] = op_name
                return result

    return result
