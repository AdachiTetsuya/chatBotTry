from .bot_base import LineBotMSG
from .bot_messages import create_text_message
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


line_message = LineBotMSG()

class LineBotApiView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        res = request.data
        response_text = {"text": "正常に検索されました。"} #レスポンスとして返す
        code = status.HTTP_200_OK #レスポンスのステータスコード
        if len(res['events']) > 0:
            data = res['events'][0] #リストの中に辞書がひとつ
            text = data['message'].get('text')

            line_message.reply(data['replyToken'], create_text_message("テスト用ボットのテキスト"))
        else:
            response_text["text"] = "Webhookの確認" #確認時に返すレスポンス
        return Response(response_text, status=code)