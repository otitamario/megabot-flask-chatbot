from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatbot import chatbot
app = Flask(__name__)

megabot=chatbot()
megabot.init()
megabot.training()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(megabot.get_reply(userText))


if __name__ == "__main__":
    app.run()