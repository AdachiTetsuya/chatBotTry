from api.about_user import save_user
from api.bot_messages import create_text_message_list, get_greeting_message
from api.utils import get_reply_token, get_user_id


def follow_event_function(line_message, event_obj):
    user_id = get_user_id(event_obj)
    user_info = line_message.get_user_info(user_id)
    reply_token = get_reply_token(event_obj)

    save_user(user_info["displayName"], user_id)

    line_message.reply(
        reply_token,
        create_text_message_list(get_greeting_message(user_info["displayName"])),
    )
