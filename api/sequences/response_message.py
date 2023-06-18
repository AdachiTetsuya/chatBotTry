from api.bot_messages import create_quick_reply_text_list, create_text_message_list
from api.models import ResponseMessage, UserPollRelation


def everyone_response(user_poll_relations):
    poll_name_list = [item.poll_name for item in user_poll_relations]
    message_list = ResponseMessage.objects.order_by("?")[: len(poll_name_list)]

    message_list = [
        "{} 「{}」".format(name, message.text)
        for (name, message) in zip(poll_name_list, message_list)
    ]
    formatted_message = "\n".join(message_list)

    choice_list = [(poll_name, f"{poll_name}〜") for poll_name in poll_name_list]

    result = create_quick_reply_text_list(formatted_message, choice_list)
    return result


def single_response(user_poll_relation: UserPollRelation):
    # relationship_level = user_poll_relation.relationship_level
    poll_age = user_poll_relation.poll_age

    message = (
        ResponseMessage.objects.filter(poll_age_min__lte=poll_age, poll_age_max__gte=poll_age)
        .order_by("?")
        .first()
    )
    formatted_message = "{}: 「{}」".format(user_poll_relation.poll_name, message.text)
    result = create_text_message_list(formatted_message)
    return result
