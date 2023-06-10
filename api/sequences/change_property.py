from api.bot_messages import create_button_list_message_list, create_text_message_list


def show_change_prop_obj_list(user_poll_relations):
    name_list = [item.poll_name for item in user_poll_relations]
    name_list.append("あなた")

    result = create_text_message_list("誰のプロパティを変更しますか？")
    button_list = create_button_list_message_list(name_list)
    result.extend(button_list)

    return result
