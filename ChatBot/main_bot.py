# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Teste')
bot.set_trainer(ListTrainer)

for arqv in os.listdir('arqv'):
    chats = open('arqv/'+arqv, 'r').readlines()
    bot.train(chats)

while True:
    resq = input('Você: ')
    resp = bot.get_response(resq)
    print('Bot: ' + str(resp))
