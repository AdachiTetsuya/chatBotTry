from api.about_user import save_user
from api.bot_messages import create_text_message_list, get_greeting_message
from api.utils import get_user_id


def follow_event_function(line_message, event_obj):
    """
    フォローイベントを受け取って、適切な送信メッセージを返す。

    Args:
        line_message (instance): Line API インターフェース のインスタンス
        event_obj (dict): Messaging API の イベントオブジェクト

    Returns:
        list[dict[str, str]] : reply メソッド用にフォーマットした送信メッセージ
    """

    user_id = get_user_id(event_obj)
    user_info = line_message.get_user_info(user_id)

    save_user(user_info["displayName"], user_id)

    sentence = get_greeting_message(user_info["displayName"])
    result = create_text_message_list(sentence)

    return result
