import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .bot_base import LineBotMSG
from .bot_messages import create_text_message_list

logger = logging.getLogger("api")


line_message = LineBotMSG()


class LineBotApiView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        res = request.data

        if res["events"]:
            data = res["events"][0]  # リストの中に辞書がひとつ
            if data["message"]:
                line_message.reply(data["replyToken"], create_text_message_list("こんにちわ", "こんばんわ"))
        else:
            response_text = {"text": "正常に検索されました。"}  # レスポンスとして返す
        return Response(response_text, status=status.HTTP_200_OK)
