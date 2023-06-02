import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .bot_base import LineBotMSG
from .bot_messages import create_text_message_list, get_greeting_message, get_random_unknown_message
from .models import CustomUser
from .utils import (
    get_event_type_name,
    get_message_text,
    get_reply_token,
    get_user_id,
    is_text_message,
)

logger = logging.getLogger("api")

line_message = LineBotMSG()


class LineBotApiView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        event_obj = request.data["events"][0]

        event_type = get_event_type_name(event_obj)

        if event_type == "message":
            user_id = get_user_id(event_obj)
            reply_token = get_reply_token(event_obj)

            if is_text_message(event_obj):
                message = get_message_text(event_obj)
                line_message.reply(reply_token, create_text_message_list(message))
            else:
                message = get_random_unknown_message()
                line_message.reply(reply_token, create_text_message_list(message))

        if event_type == "follow":
            user_id = get_user_id(event_obj)
            user_info = line_message.get_user_info(user_id)
            reply_token = get_reply_token(event_obj)

            CustomUser.objects.create(username=user_info["displayName"], line_id=user_id)

            line_message.reply(
                reply_token,
                create_text_message_list(get_greeting_message(user_info["displayName"])),
            )
        return Response({"text": "正常に検索されました。"}, status=status.HTTP_200_OK)
