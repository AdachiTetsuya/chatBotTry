from django.db.models.signals import post_save
from django.dispatch import receiver

from api.bot_base import LineBotMSG
from api.bot_messages import create_text_message_list
from api.models import BroadCastMessage

line_message = LineBotMSG()


@receiver(post_save, sender=BroadCastMessage)
def publish_broadcast_message(sender, instance, created, **kwargs):
    if instance.on_publish:
        message = create_text_message_list(instance.text)
        line_message.broad_cast_message(message)
