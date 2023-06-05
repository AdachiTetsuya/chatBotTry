from api.bot_messages import create_text_message_list
from api.models import ResponseMessage


def everyone_response(user_poll_relations):
    poll_name_list = [item.poll_name for item in user_poll_relations]
    message_list = ResponseMessage.objects.order_by("?")[: len(poll_name_list)]

    message_list = [
        "{} 「{}」".format(name, message.text)
        for (name, message) in zip(poll_name_list, message_list)
    ]
    formatted_message = "\n".join(message_list)
    result = create_text_message_list(formatted_message)
    return result


def single_response(user_poll_relation):
    message = ResponseMessage.objects.order_by("?").first()
    formatted_message = "{}: 「{}」".format(user_poll_relation.poll_name, message.text)
    result = create_text_message_list(formatted_message)
    return result
