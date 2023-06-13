import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.about_user import get_related_instance
from api.data.sticker_data import get_random_sticker
from api.sequences.on_follow import follow_event_function
from api.sequences.receive_message import receive_message_function

from .bot_base import LineBotMSG
from .bot_messages import (
    create_sticker_message_list,
    create_text_message_list,
    get_random_unknown_message,
)
from .utils import get_event_type_name, get_message_type, get_reply_token

logger = logging.getLogger("api")

line_message = LineBotMSG()


class LineBotApiView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        event_obj = request.data["events"][0]

        event_type = get_event_type_name(event_obj)

        if event_type == "message":
            reply_token = get_reply_token(event_obj)
            user, user_poll_relations = get_related_instance(event_obj)

            # manage_property_input(event_obj)

            message_type = get_message_type(event_obj)

            if message_type == "text":
                message = receive_message_function(event_obj, user, user_poll_relations)
                line_message.reply(reply_token, message)

            elif message_type == "sticker":
                message = create_sticker_message_list(get_random_sticker())
                line_message.reply(reply_token, message)
                pass

            else:
                message = get_random_unknown_message()
                line_message.reply(reply_token, create_text_message_list(message))
                return Response(status=status.HTTP_200_OK)

        if event_type == "follow":
            reply_token = get_reply_token(event_obj)

            message = follow_event_function(line_message, event_obj)
            line_message.reply(reply_token, message)

        return Response(status=status.HTTP_200_OK)
