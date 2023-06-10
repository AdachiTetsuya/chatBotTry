from api.bot_messages import create_button_template_message_list


def show_MB_operation_list(user_poll_relations):
    choice_list = []
    for user_poll in user_poll_relations:
        if user_poll.is_buddy:
            choice_list.append("{}を ByBuddy から解除".format(user_poll.poll_name))
        else:
            choice_list.append("{}を ByBuddy に登録".format(user_poll.poll_name))

    result = create_button_template_message_list(choice_list)
    return result
