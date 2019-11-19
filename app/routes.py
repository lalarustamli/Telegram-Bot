from flask import request
from app import app
from app import bot
import telegram

@app.route("/")
def hello_world():
    return 'Hello, World!'


@app.route("/webhook", methods=['GET', 'POST'])
def listen():
    if request.method == "POST":
        text = ''
        chat_id, text, update_id = bot.get_last_id_text(get_updates())
        chat_id, text, update_id = bot.start(chat_id)
        print('Started')
    # if request.method == "GET":
    #     return chatbot.verify_webhook(request)

    # if request.method == "POST":
    #     events = request.json['entry'][0]['messaging']
    #     for event in events:
    #         print(str(event))
    #         if chatbot.is_user_message(event):
    #             print(str("yes"))
    #             chatbot.respond(event)
    #         elif chatbot.is_user_postback(event):
    #             chatbot.postback_response(event)
    #
    #     return "user message"
