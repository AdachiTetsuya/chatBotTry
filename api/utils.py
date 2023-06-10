def get_event_type_name(event_obj):
    event_type = event_obj["type"]
    return event_type


def get_user_line_id(event_obj):
    user_line_id = event_obj["source"]["userId"]
    return user_line_id


def get_message_type(event_obj):
    message_type = event_obj["message"]["type"]
    return message_type


def get_message_text(event_obj):
    message = event_obj["message"]["text"]
    return message


def get_reply_token(event_obj):
    reply_token = event_obj["replyToken"]
    return reply_token


def judge_comment_from_temperature(temperature):
    result = ""

    if temperature < 0:
        result = "めっちゃ寒いっすね。"
    elif temperature >= 0 and temperature < 10:
        result = "寒いっすね"
    elif temperature >= 10 and temperature < 20:
        result = "ちょうど良いっすね。"
    elif temperature >= 20 and temperature < 30:
        result = "あったかいっすね。"
    elif temperature >= 30 and temperature < 40:
        result = "暑いっすね。"
    elif temperature <= 40:
        result = "めっちゃ暑いっすね。"

    return result


def get_primary_poll(user_poll_relations):
    result = ""

    for user_poll in user_poll_relations:
        if user_poll.is_primary:
            result = user_poll

    return result


def get_buddy_not_primary_poll(user_poll_relations):
    buddy_poll_list = [
        user_poll
        for user_poll in user_poll_relations
        if user_poll.is_buddy and not user_poll.is_primary
    ]
    return buddy_poll_list
