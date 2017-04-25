import sys

import telegram
from flask import Flask, request


API_TOKEN = 'Your Telegram API Token'
WEBHOOK_URL = 'Your Webhook URL'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    text = update.message.text
    update.message.reply_text(text)
    return 'ok'


if __name__ == "__main__":
    _set_webhook()
    app.run()
