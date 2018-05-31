# # !/usr/bin/python
# # -*- coding: utf-8 -*-
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# chatbot = ChatBot("myBot")
# chatbot.set_trainer(ChatterBotCorpusTrainer)
#
# # 使用英文语料库训练它
# chatbot.train("chatterbot.corpus.english")
#
# # 开始对话
# while True:
#     print(chatbot.get_response(input(">")))
#
# ##########################################
# # -*- coding: utf-8 -*-
#
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
# import logging
# # Uncomment the following line to enable verbose logging
#
# #logging.basicConfig(level=logging.INFO)
#
# # Create a new ChatBot instance
#
# chatbot = ChatBot(
#     'Norman',
# storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
#
# logic_adapters=[
#  'chatterbot.logic.BestMatch',
#  'chatterbot.logic.MathematicalEvaluation',
#  'chatterbot.logic.TimeLogicAdapter'
# ],
#     filters=[
#  'chatterbot.filters.RepetitiveResponseFilter'
#   ],
#
#     input_adapter="chatterbot.input.TerminalAdapter",
#     output_adapter="chatterbot.output.TerminalAdapter",
#     trainer='chatterbot.trainers.ListTrainer',
#     database="chatterbot-1w",
#     database_uri="mongodb://localhost:27017/",
#     read_only=True
# )
#
# print('Type something to begin...')
#
# while True:
#     try:
#         bot_input = chatbot.get_response(None)
#
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break;
#
#
#
# # pip install chatterbot