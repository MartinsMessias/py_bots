# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot, corpus, languages
from telegram.ext import Updater, CommandHandler, RegexHandler
import os


bot_ = ChatBot('BotName')

trainer = ChatterBotCorpusTrainer(bot_)

# Alternar para esse caso queira treinar de um arquivo
# bot_.set_trainer(ListTrainer)
# trainer = ListTrainer(bot_)

# Treina baseado em um dicionário de frases definidas
trainer.train(
    'chatterbot.corpus.portuguese.compliment',
    'chatterbot.corpus.portuguese.conversations',
    'chatterbot.corpus.portuguese.games',
    'chatterbot.corpus.portuguese.greetings',
    'chatterbot.corpus.portuguese.money',
)

# Alternar para esse caso queira que ele treine 
# as frases de um arquivo em específico
#for arqv in os.listdir('arqv'):
#   chats = open('arqv/' + arqv, 'r').readlines()


def func(bot, update):
    resq = update['message']['text']
    update.message.reply_text(
        '{}'.format(bot_.get_response(resq)))


updater = Updater('TELEGRAM_TOKEN')
updater.dispatcher.add_handler(RegexHandler('', func))
updater.start_polling()
updater.idle()

