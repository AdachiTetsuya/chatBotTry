from api.bot_messages import create_button_list_message_list, create_text_message_list
from api.models import CustomUser, UserPollRelation, UserSequence


def show_change_prop_obj_list(user_poll_relations):
    name_list = [(item.poll_name, f"{item.poll_name}のプロパティを変更します") for item in user_poll_relations]
    name_list.append(("あなた", "私のプロパティを変更します"))

    result = create_text_message_list("誰のプロパティを変更しますか？")
    button_list = create_button_list_message_list(name_list)
    result.extend(button_list)

    return result


def show_change_prop_list(target):
    choice_list = ""
    if isinstance(target, UserPollRelation):
        property_list = ["名前", "年齢", "性別"]
        choice_list = [(item, f"{target.poll_name}の{item}を変更します") for item in property_list]
    elif isinstance(target, CustomUser):
        choice_list = [("名前", "私の名前を変更します")]

    result = create_text_message_list("どのプロパティを変更しますか？")
    button_list = create_button_list_message_list(choice_list)
    result.extend(button_list)

    return result


def new_name_input_prompt(user: CustomUser):
    (user_sequence,) = UserSequence.objects.get_or_create(user=user)
    user_sequence.is_change_poll_name = True
    user_sequence.save()

    result = create_text_message_list("新しい名前を入力してください。")
    return result
