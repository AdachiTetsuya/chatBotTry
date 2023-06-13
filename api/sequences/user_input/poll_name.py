from api.bot_messages import create_text_message_list
from api.models import CustomUser, UserPollRelation, UserSequence


def change_poll_name(
    message,
    user: CustomUser,
    user_sequence: UserSequence,
    user_poll_relations: list[UserPollRelation],
):
    # validation
    if len(message) > 30:
        return create_text_message_list("名前が長すぎます。")

    name_list = [item.poll_name for item in user_poll_relations]
    name_list.append(user.username)
    if message in name_list:
        return create_text_message_list(f"{message}という名前は重複があります。")

    poll: UserPollRelation = user_sequence.target
    pre_name = poll.poll_name
    new_name = message
    poll.poll_name = new_name
    poll.save()

    return create_text_message_list(f"{pre_name}の名前を{new_name}に変更しました")
