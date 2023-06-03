import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.sequences.on_follow import follow_event_function
from api.sequences.receive_message import receive_message_function

from .bot_base import LineBotMSG
from .bot_messages import create_text_message_list, get_random_unknown_message
from .utils import get_event_type_name, get_reply_token, get_user_line_id, is_text_message

logger = logging.getLogger("api")

line_message = LineBotMSG()


class LineBotApiView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        event_obj = request.data["events"][0]

        event_type = get_event_type_name(event_obj)

        if event_type == "message":
            reply_token = get_reply_token(event_obj)

            if not is_text_message(event_obj):
                message = get_random_unknown_message()
                line_message.reply(reply_token, create_text_message_list(message))
                return Response(status=status.HTTP_200_OK)

            message = receive_message_function(event_obj)
            line_message.reply(reply_token, message)

        if event_type == "follow":
            reply_token = get_reply_token(event_obj)

            message = follow_event_function(line_message, event_obj)
            line_message.reply(reply_token, message)

        line_message.push_message(get_user_line_id(event_obj), create_text_message_list("さようなら"))

        return Response(status=status.HTTP_200_OK)
