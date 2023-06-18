from api.bot_messages import create_quick_reply_text_list, create_text_message_list
from api.models import UserPollRelation, UserSequence


def validate_input(message):
    error_msg = ""
    if not message.isnumeric():
        error_msg = "入力された値が数値ではありません"

    elif message < 0 or message > 130:
        error_msg = "年齢は 0歳以上、130歳以下で入力してください"

    return error_msg


def change_poll_age(
    message,
    user_sequence: UserSequence,
):
    # validation
    if error_msg := validate_input(message):
        result = create_text_message_list(error_msg)
        result.extend(create_quick_reply_text_list("新しい年齢を入力してください。", [("キャンセル", "中断します")]))
        return result

    poll: UserPollRelation = user_sequence.target
    new_age = message
    poll.poll_age = new_age
    poll.save()

    user_sequence.is_change_poll_age = False
    user_sequence.save()

    return create_text_message_list(f"{poll.poll_name} の年齢を {new_age}に変更しました")
