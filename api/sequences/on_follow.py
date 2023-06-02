import logging

from api.about_user import create_user_poll_relation, save_user
from api.bot_messages import create_text_message_list, get_greeting_message, get_introduce_message
from api.utils import get_user_line_id

logger = logging.getLogger("api")


def follow_event_function(line_message, event_obj):
    """
    フォローイベントを受け取って、適切な送信メッセージを返す。

    Args:
        line_message (instance): Line API インターフェース のインスタンス
        event_obj (dict): Messaging API の イベントオブジェクト

    Returns:
        list[dict[str, str]] : reply メソッド用にフォーマットした送信メッセージ
    """

    user_id = get_user_line_id(event_obj)
    user_info = line_message.get_user_info(user_id)

    user_instance = save_user(user_info["displayName"], user_id)

    user_poll_relation_queryset = create_user_poll_relation(user_instance, user_id)
    logger.info(user_poll_relation_queryset)

    greeting_message = get_greeting_message(user_info["displayName"])
    introduce_message = get_introduce_message(user_poll_relation_queryset)
    result = create_text_message_list(greeting_message, introduce_message)

    return result
