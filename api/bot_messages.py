from .models import GreetingMessage, UnknownMessage


def create_text_message_list(*args):
    if args:
        message = [{"type": "text", "text": msg} for msg in args]
    return message


def get_greeting_message(displayName):
    message = GreetingMessage.objects.order_by("?").first()
    text = message.text
    formatted_text = text.replace(r"{displayName}", displayName)
    return formatted_text


def get_random_unknown_message():
    message = UnknownMessage.objects.order_by("?").first()
    return message.text
