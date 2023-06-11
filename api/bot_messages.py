from .models import GreetingMessage, UnknownMessage


def create_text_message_list(*args):
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


def create_button_list_message_list(choice_list):
    """
    Args
        list(str(label))
        list(tuple(label,text))
    """
    contents_list = []
    for item in choice_list:
        if type(item) is str:
            content = {
                "type": "button",
                "action": {"type": "message", "label": item, "text": item},
            }
            contents_list.append(content)
        else:
            content = {
                "type": "button",
                "action": {"type": "message", "label": item[0], "text": item[1]},
            }
            contents_list.append(content)

    message = {
        "type": "flex",
        "altText": "flexMessageです",
        "contents": {
            "type": "bubble",
            "body": {"type": "box", "layout": "vertical", "contents": contents_list},
        },
    }
    return [message]


def create_quick_reply_text_list(text: str, choice_list):
    item_list = []
    for choice in choice_list:
        if type(choice) is str:
            content = {
                "type": "action",
                "action": {"type": "message", "label": choice, "text": choice},
            }
            item_list.append(content)
        else:
            content = {
                "type": "action",
                "action": {"type": "message", "label": choice[0], "text": choice[1]},
            }
            item_list.append(content)
    message = {
        "type": "text",
        "text": text,
        "quickReply": {"items": item_list},
    }
    return [message]


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
