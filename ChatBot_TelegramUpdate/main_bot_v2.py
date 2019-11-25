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






















# # -*- coding: utf- -*-
#
# import urllib
# import urllib2
#
# url = "http://sandbox.api.simsimi.com/request.p?"
#
# text_input = raw_input("Input your text: ")
# lc_input = raw_input("Input your lc: ")
# text = text_input.encode("utf-8")
# lc = lc_input.encode("utf-8")
# values = {'key' : 'ykKEPX6rXijNxrCppGh3kxgd8MNetA5Fvmeyuea0',
#           'lc' : lc,
#           'ft' : '0.0',
# 	      'text' : text}
#
# data = urllib.urlencode(values)
# request_url = urllib2.Request(url, data)
# response_post = urllib2.urlopen(request_url)
# response = response_post.read().decode("utf-8")
# print response