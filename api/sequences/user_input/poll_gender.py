from api.bot_messages import create_quick_reply_button_list, create_text_message_list
from api.data.constants import POLL_GENDER_LIST, POLL_GENDER_TUPLE_LIST
from api.models import UserPollRelation, UserSequence


def convert_gender_to_num(gender_str):
    for tuple_item in POLL_GENDER_TUPLE_LIST:
        if tuple_item[1] == gender_str:
            return tuple_item[0]


def validate_input(message):
    error_msg = ""

    if message not in POLL_GENDER_LIST:
        error_msg = "入力された値が選択肢にありません"

    return error_msg


def change_poll_gender(
    message: str,
    user_sequence: UserSequence,
):
    # validation
    if error_msg := validate_input(message):
        result = create_text_message_list(error_msg)
        result.extend(create_quick_reply_button_list(POLL_GENDER_LIST, [("キャンセル", "中断します")]))
        return result

    poll: UserPollRelation = user_sequence.target
    new_gender = message
    poll.poll_gender = convert_gender_to_num(new_gender)
    poll.save()

    user_sequence.is_change_poll_gender = False
    user_sequence.save()

    return create_text_message_list(f"{poll.poll_name} の性別を {new_gender} に変更しました")
