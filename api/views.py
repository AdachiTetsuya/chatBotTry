import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.sequences.follow import follow_event_function

from .bot_base import LineBotMSG
from .bot_messages import create_text_message_list, get_random_unknown_message
from .utils import get_event_type_name, get_message_text, get_reply_token, is_text_message

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

            message = get_message_text(event_obj)
            line_message.reply(reply_token, create_text_message_list(message))

        if event_type == "follow":
            follow_event_function(line_message, event_obj)

        return Response(status=status.HTTP_200_OK)
