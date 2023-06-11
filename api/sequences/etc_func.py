from api.bot_messages import (
    create_image_message_list,
    create_quick_reply_text_list,
    create_text_message_list,
)
from api.models import SmartPoll
from api.utils import judge_comment_from_temperature


def sky_photo():
    if smart_poll := SmartPoll.objects.filter(can_sky_photo=True).first():
        url = smart_poll.get_sky_photo()
        text_list = create_text_message_list("今日の空の写真です")
        image_list = create_image_message_list(url)
        text_list.extend(image_list)
        return text_list


def show_temperature():
    smart_poll = SmartPoll.objects.first()
    temperature = smart_poll.get_temperature()
    comment = judge_comment_from_temperature(temperature)
    text_list = create_text_message_list(f"今日の気温は{temperature}度です。{comment}")
    dialog = create_quick_reply_text_list("もっと知りたいですか？", ["はい", "いいえ"])
    text_list.extend(dialog)
    return text_list
