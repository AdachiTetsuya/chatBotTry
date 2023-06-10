from api.bot_messages import create_button_list_message_list, create_text_message_list


def show_change_prop_obj_list(user_poll_relations):
    name_list = [(item.poll_name, f"{item.poll_name}のプロパティを変更します") for item in user_poll_relations]
    name_list.append(("あなた", "私のプロパティを変更します"))

    result = create_text_message_list("誰のプロパティを変更しますか？")
    button_list = create_button_list_message_list(name_list)
    result.extend(button_list)

    return result
