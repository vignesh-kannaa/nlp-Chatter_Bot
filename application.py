from flask import Flask, jsonify, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)

conversation = [
    "Hey Luna",
    "Hi. Your virtual personal navigator for this building",
    "That's great. What can you do?",
    "I can guide from your current place to your desired place within this building",
    "Can you navigate me to 301",
    "Sorry I'm currently instructed to navigate from 212 to 216 for testing purpose",
    "ok. I understand. Can you guide me to 212",
    "Sure. Please follow me to 212",
    "Can you guide me to 214f",
    "Ok. Follow me to 214f",
]
trainer = ListTrainer(english_bot)
trainer.train(conversation)

trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_response():
    userText = request.args.get('msg')
    print('user text: ', userText)
    return str(english_bot.get_response(userText))


@app.route("/api/chat", methods=["POST"])
def get_chat_response():
    data = request.get_json()
    userText = data.get('msg')
    return jsonify({"response": str(english_bot.get_response(userText))})


if __name__ == "__main__":
    app.run()


# Setup and run
# conda create -p venv python==3.9 -y
# conda activate pathto/venv
# python -m pip install chatterbot==1.0.4 pytz
# pip instal flask
# python application.py
    # or
# PS> python -m venv venv
# PS> venv\Scripts\activate
# (venv) PS> python -m pip install chatterbot==1.0.4 pytz
# python application.py
