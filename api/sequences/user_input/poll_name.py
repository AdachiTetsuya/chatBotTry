from api.bot_messages import create_quick_reply_text_list, create_text_message_list
from api.models import CustomUser, UserPollRelation, UserSequence


def get_pre_name(target: UserPollRelation | CustomUser):
    if isinstance(target, UserPollRelation):
        return target.poll_name
    return "あなた"


def save_name_func(target: UserPollRelation | CustomUser, new_name):
    if isinstance(target, UserPollRelation):
        target.poll_name = new_name
    else:
        target.username = new_name
    target.save()


def validate_input(message, name_list):
    error_msg = ""
    if len(message) > 30:
        error_msg = "名前が長すぎます。"

    if message in name_list:
        error_msg = f"{message} という名前は重複があります。"

    return error_msg


def change_name(
    message,
    user: CustomUser,
    user_sequence: UserSequence,
    user_poll_relations: list[UserPollRelation],
):
    # validation
    name_list = [item.poll_name for item in user_poll_relations]
    name_list.append(user.username)
    if error_msg := validate_input(message, name_list):
        result = create_text_message_list(error_msg)
        result.extend(create_quick_reply_text_list("新しい名前を入力してください。", [("キャンセル", "中断します")]))
        return result

    target: UserPollRelation | None = user_sequence.target
    if not target:
        target = user

    pre_name = get_pre_name(target)
    new_name = message
    save_name_func(target, new_name)

    user_sequence.is_change_name = False
    user_sequence.save()

    return create_text_message_list(f"{pre_name}の名前を {new_name} に変更しました")
