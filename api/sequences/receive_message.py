from api.bot_messages import create_text_message_list


def receive_message_function(event_obj):
    """
    テキストメッセージを受け取って、適切な送信メッセージを返す。

    Args:
        event_obj (dict): Messaging API の イベントオブジェクト

    Returns:
        list[dict[str, str]] : reply メソッド用にフォーマットした送信メッセージ
    """

    sequence = judge_sequence_from_message(event_obj)

    if sequence == 1:
        result = create_text_message_list("メッセージ")
        return result


def judge_sequence_from_message(event_obj):
    return 1
