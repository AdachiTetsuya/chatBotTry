import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .bot_base import LineBotMSG
from .bot_messages import create_text_message_list
from .utils import get_event_type_name, get_message_text, get_reply_token

logger = logging.getLogger("api")


line_message = LineBotMSG()


class LineBotApiView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        event_obj = request.data["events"][0]

        event_type = get_event_type_name(event_obj)

        if event_type == "message":
            message = get_message_text(event_obj)
            line_message.reply(get_reply_token(event_obj), create_text_message_list(message))

        if event_type == "follow":
            line_message.reply(get_reply_token(event_obj), create_text_message_list("こんにちわ"))
        else:
            response_text = {"text": "正常に検索されました。"}  # レスポンスとして返す
        return Response(response_text, status=status.HTTP_200_OK)
