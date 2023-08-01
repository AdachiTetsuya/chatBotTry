from chatterbot import ChatBot

# from chatterbot.trainers import ChatterBotCorpusTrainer
import languages  # 自作言語モジュール

chatbot = ChatBot(
    "test",
    tagger_language=languages.GINZA,
    database_uri="sqlite:///database.db",
)

response = chatbot.get_response("調子はどう？")
