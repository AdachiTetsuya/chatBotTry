from api.bot_messages import create_button_list_message_list, create_text_message_list


def show_MB_operation_list(user_poll_relations):
    choice_list = []
    for user_poll in user_poll_relations:
        if user_poll.is_buddy:
            choice_list.append("{}を MyBuddy から解除".format(user_poll.poll_name))
        else:
            choice_list.append("{}を MyBuddy に登録".format(user_poll.poll_name))

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
