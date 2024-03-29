import logging

from chatterbot import ChatBot

from api.utils import get_message_text

logger = logging.getLogger("api")

chatbot = ChatBot(
    "test",
    database_uri="sqlite:///database.db",
)


def get_chatterbot_message(event_obj):
    message = get_message_text(event_obj)
    response = chatbot.get_response(message)
    response_data = response.serialize().get("text")

    return response_data
