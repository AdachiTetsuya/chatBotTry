from api.bot_messages import (
    create_button_list_message_list,
    create_quick_reply_text_list,
    create_text_message_list,
)
from api.models import CustomUser, UserPollRelation, UserSequence


def show_all_property(user_poll_relations: list[UserPollRelation], user: CustomUser):
    text_all = ""
    for poll in user_poll_relations:
        prop_list = [
            poll.poll_name,
            f"年齢: {poll.poll_age}歳",
            f"性別: {poll.poll_gender}",
            f"バディか: {poll.is_buddy}",
        ]
        if poll.is_buddy:
            prop_list.append(f"プライマリーか: {poll.is_primary}")

        text = "\n".join(prop_list)
        text_all += text
        text_all += "\n\n"
    user_prop_list = ["あなた", f"名前: {user.username}"]
    text_all += "\n".join(user_prop_list)

    choice_list = [("はい", "プロパティを変更します"), ("いいえ", "いいえ")]
    result = create_text_message_list(text_all)
    result.extend(create_quick_reply_text_list("プロパティを変更しますか？", choice_list))

    return result


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


def new_name_input_prompt(target: UserPollRelation | CustomUser, user: CustomUser):
    user_sequence = UserSequence.objects.get(user=user)
    user_sequence.is_change_poll_name = True
    if isinstance(target, UserPollRelation):
        user_sequence.target = target
    user_sequence.save()

    result = create_text_message_list("新しい名前を入力してください。")
    return result
