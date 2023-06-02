def get_event_type_name(event_obj):
    event_type = event_obj["type"]
    return event_type


def is_text_message(event_obj):
    message_type = event_obj["message"]["type"]
    if message_type == "text":
        return True
    return False


def get_message_text(event_obj):
    message = event_obj["message"]["text"]
    return message


def get_reply_token(event_obj):
    reply_token = event_obj["replyToken"]
    return reply_token


def get_user_id(event_obj):
    user_id = event_obj["source"]["userId"]
    return user_id
