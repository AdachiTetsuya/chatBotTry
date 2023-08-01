from chatterbot import ChatBot

from api.utils import get_message_text

chatbot = ChatBot(
    "test",
    database_uri="sqlite:///database.db",
)


def get_chatterbot_message(event_obj):
    message = get_message_text(event_obj)
    response = chatbot.get_response(message)
    return response
