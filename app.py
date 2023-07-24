from flask import Flask, jsonify, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")
conversation = [
    "Hello",
    "Hey, I'm Luna. Your virtual personal navigator for this building",
    "That's great. What can you do?",
    "I can guide from your current place to your desired place within this building",
    "Can you navigate me to 301",
    "Sorry I'm currently instructed to navigate from 212 to 216 for testing purpose",
    "ok. I understand. Can you guide me to 212"
    "Sure. Please follow me to 212"
]
trainer = ListTrainer(english_bot)
trainer.train(conversation)


# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route("/chat", methods=["POST"])
def get_bot_response():
    # userText = request.args.get('msg')
    # return str(english_bot.get_response(userText))
    data = request.get_json()
    userText = data.get('msg')
    return jsonify({"response": str(english_bot.get_response(userText))})


if __name__ == "__main__":
    app.run()
