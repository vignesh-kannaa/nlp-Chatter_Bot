from flask import Flask, jsonify, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json


app = Flask(__name__)


# Load conversation data from JSON file
with open('training-conversation.json', 'r') as json_file:
    conversation_data = json.load(json_file)

conversation = []
for pair in conversation_data:
    conversation.append(pair['input'])
    conversation.append(pair['output'])

print('conversation:', conversation)

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)


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
