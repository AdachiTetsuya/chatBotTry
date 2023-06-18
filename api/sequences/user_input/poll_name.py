from api.bot_messages import create_quick_reply_text_list, create_text_message_list
from api.models import CustomUser, UserPollRelation, UserSequence


def validate_input(message, name_list):
    error_msg = ""
    if len(message) > 30:
        error_msg = "名前が長すぎます。"

    if message in name_list:
        error_msg = f"{message}という名前は重複があります。"

    return error_msg


def change_poll_name(
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

    poll: UserPollRelation = user_sequence.target
    pre_name = poll.poll_name
    new_name = message
    poll.poll_name = new_name
    poll.save()

    user_sequence.is_change_poll_name = False
    user_sequence.save()

    return create_text_message_list(f"{pre_name}の名前を{new_name}に変更しました")
