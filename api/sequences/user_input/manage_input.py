from api.bot_messages import create_text_message_list
from api.models import UserSequence
from api.utils import get_message_text, get_message_type

from .poll_name import change_poll_name


def manage_property_input(event_obj, user, user_poll_relations):
    user_sequence = UserSequence.objects.get(user=user)
    message_type = get_message_type(event_obj)

    if not user_sequence.is_inputting:
        return

    if message_type != "text":
        return create_text_message_list("有効な文字列を入力してください")

    message = get_message_text(event_obj)
    if user_sequence.is_change_poll_name:
        return change_poll_name(message, user, user_sequence, user_poll_relations)
