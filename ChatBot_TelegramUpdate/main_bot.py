# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from telegram.ext import Updater, CommandHandler, RegexHandler
import os

ativ = True
bot_ = ChatBot('Clovis')
bot_.set_trainer(ListTrainer)

for arqv in os.listdir('arqv'):
    chats = open('arqv/' + arqv, 'r').readlines()
    bot_.train(chats)


def hello(bot, update):
    resq = update['message']['text']
    print('Response: ', resq)
    update.message.reply_text(
        '{}'.format(bot_.get_response(resq)))


updater = Updater('TELEGRAM TOKEM')

updater.dispatcher.add_handler(RegexHandler('', hello))
updater.start_polling()
updater.idle()
