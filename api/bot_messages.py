from .models import GreetingMessage, UnknownMessage


def create_text_message_list(*args):
    if args:
        message = [{"type": "text", "text": msg} for msg in args]
    return message


def create_image_message_list(*args):
    if args:
        message = [
            {"type": "image", "originalContentUrl": url, "previewImageUrl": url} for url in args
        ]
    return message


def create_sticker_message_list(*args):
    if args:
        message = [
            {"type": "sticker", "packageId": tuple_item[0], "stickerId": tuple_item[1]}
            for tuple_item in args
        ]
    return message


def get_greeting_message(displayName):
    message = GreetingMessage.objects.order_by("?").first()
    text = message.text
    formatted_text = text.replace(r"{displayName}", displayName)
    return formatted_text


def get_introduce_message(user_poll_relation_queryset):
    name_list = [item.poll_name for item in user_poll_relation_queryset]
    text = "、".join(name_list)
    text += "が担当します"
    return text


def get_random_unknown_message():
    message = UnknownMessage.objects.order_by("?").first()
    return message.text
