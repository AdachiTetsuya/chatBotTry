from celery import shared_task

from api.bot_base import LineBotMSG
from api.bot_messages import create_text_message_list

line_message = LineBotMSG()


@shared_task
def say_hello():
    result = create_text_message_list("こんにちわ")
    id = "U9832203d5f9ab9edecff7fb10b003d77"

    line_message.push_message(id, result)
