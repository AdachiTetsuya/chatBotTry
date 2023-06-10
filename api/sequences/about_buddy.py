import logging

from api.bot_messages import create_button_list_message_list, create_text_message_list
from api.utils import get_buddy_not_primary_poll, get_primary_poll

logger = logging.getLogger("api")


def show_MB_operation_list(user_poll_relations):
    choice_list = []

    if primary_poll := get_primary_poll(user_poll_relations):
        choice_list.append("{}を プライマリー から解除".format(primary_poll.poll_name))

    elif buddy_poll_list := get_buddy_not_primary_poll(user_poll_relations):
        if len(buddy_poll_list) >= 2:
            for buddy_poll in buddy_poll_list:
                choice_list.append("{}を プライマリー に登録".format(buddy_poll.poll_name))

    for user_poll in user_poll_relations:
        if user_poll.is_buddy:
            choice_list.append("{}を MyBuddy から解除".format(user_poll.poll_name))
        else:
            choice_list.append("{}を MyBuddy に登録".format(user_poll.poll_name))

    choice_list.sort()
    result = create_text_message_list("実行したい内容を選択してください。")
    button_list = create_button_list_message_list(choice_list)
    result.extend(button_list)

    return result


def register_MB(user_poll):
    if user_poll.is_buddy:
        return create_text_message_list("{}は MyBuddy に登録済みです。".format(user_poll.poll_name))

    user_poll.is_buddy = True
    user_poll.save()

    result = create_text_message_list("{}を MyBuddy に登録しました。".format(user_poll.poll_name))
    return result


def remove_MB(user_poll):
    if not user_poll.is_buddy:
        return create_text_message_list("{}は MyBuddy に登録されていません。".format(user_poll.poll_name))

    user_poll.is_buddy = False
    user_poll.save()

    result = create_text_message_list("{}を MyBuddy から解除しました。".format(user_poll.poll_name))
    return result
