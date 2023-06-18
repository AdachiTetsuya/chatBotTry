from api.bot_messages import create_quick_reply_text_list, create_text_message_list
from api.models import CustomUser, UserSequence
from api.utils import get_message_text, get_message_type

from .poll_age import change_poll_age
from .poll_gender import change_poll_gender
from .poll_name import change_poll_name


def cancel_property_change(user: CustomUser):
    """キャンセル時の処理"""
    user_sequence = UserSequence.objects.get(user=user)
    user_sequence.is_change_user_name = (
        user_sequence.is_change_poll_name
    ) = user_sequence.is_change_poll_age = user_sequence.is_change_poll_gender = False
    user_sequence.save()

    result = create_text_message_list("中断しました")
    return result


def manage_property_input(event_obj, user, user_poll_relations):
    user_sequence = UserSequence.objects.get(user=user)
    message_type = get_message_type(event_obj)

    if not user_sequence.is_inputting:
        return

    if message_type != "text":
        return create_quick_reply_text_list("有効な文字列を入力してください。", [("キャンセル", "中断します")])

    message = get_message_text(event_obj)

    if message == "中断します":
        return cancel_property_change(user)

    if user_sequence.is_change_poll_name:
        return change_poll_name(message, user, user_sequence, user_poll_relations)

    if user_sequence.is_change_poll_age:
        return change_poll_age(message, user_sequence)

    if user_sequence.is_change_poll_gender:
        return change_poll_gender(message, user_sequence)
