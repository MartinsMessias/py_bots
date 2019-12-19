import requests
from telegram.ext import Updater, CommandHandler, RegexHandler
# SIMSIMI IA INTEGRATION
headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'YOUR KEY',
}

def func(bot, update):
    say = update['message']['text']
    data = '{\n           "utext": "' + say + '", \n            "lang": "pt" \n     }'
    response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=headers, data=data)
    update.message.reply_text('{}'.format(response.json()['atext']))


updater = Updater('TELEGRAM TOKEN')
updater.dispatcher.add_handler(RegexHandler('', func))
updater.start_polling()
updater.idle()
