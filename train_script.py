from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "test",
    database_uri="sqlite:///database.db",
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.japanese")

response = chatbot.get_response("調子はどう？")
print(response)
