from .models import GreetingMessage, UnknownMessage


def create_text_message_list(*args):
    if args:
        message = [{"type": "text", "text": msg} for msg in args]
    return message


def get_greeting_message(displayName):
    message = GreetingMessage.objects.order_by("?").first()
    formatted_message = message.replace(r"{displayName}", displayName)
    return formatted_message


def get_random_unknown_message():
    message = UnknownMessage.objects.order_by("?").first()
    return message.text
