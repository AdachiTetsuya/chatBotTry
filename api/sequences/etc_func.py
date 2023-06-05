from api.bot_messages import create_image_message_list, create_text_message_list
from api.models import SmartPoll


def sky_photo():
    if smart_poll := SmartPoll.objects.filter(can_sky_photo=True).first():
        url = smart_poll.get_sky_photo()
        text_list = create_text_message_list("今日の空の写真です")
        image_list = create_image_message_list(url)
        text_list.extend(image_list)
        return text_list
