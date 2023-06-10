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

    result = create_text_message_list("実行したい内容を選択してください。")
    button_list = create_button_list_message_list(sorted(choice_list, reverse=True))
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


def register_primary(user_poll, user_poll_relations):
    if primary_poll := get_primary_poll(user_poll_relations):
        if primary_poll.poll_name == user_poll.poll_name:
            return create_text_message_list("{}は プライマリー に登録済みです。".format(user_poll.poll_name))
        else:
            return create_text_message_list(
                "すでに{}がプライマリーに登録済みです。2人以上をプライマリーに指定することはできません。".format(primary_poll.poll_name)
            )
    else:
        buddy_poll_list = get_buddy_not_primary_poll(user_poll_relations)
        if len(buddy_poll_list) <= 1:
            return create_text_message_list("誰かとプライマリーになるためには、2人以上を MyBuddy に登録する必要があります。")
        else:
            if not user_poll.is_buddy:
                return create_text_message_list(
                    "{}はまだ MyBuddy に登録されていません。MyBuddy に登録されている人だけが プライマリーに登録できます。".format(
                        user_poll.poll_name
                    )
                )
            else:
                user_poll.is_primary = True
                user_poll.save()
                return create_text_message_list("{}を プライマリー に登録しました。".format(user_poll.poll_name))


def remove_primary(user_poll, user_poll_relations):
    if primary_poll := get_primary_poll(user_poll_relations):
        if primary_poll.poll_name == user_poll.poll_name:
            user_poll.is_primary = False
            user_poll.save()
            return create_text_message_list("{}を プライマリー から解除しました。".format(user_poll.poll_name))

    return create_text_message_list("{}は プライマリー に登録されていません。".format(user_poll.poll_name))
