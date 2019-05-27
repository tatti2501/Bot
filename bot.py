from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level = logging.INFO, filename='bot.log')

def greet_user(bot, update):
    print('Вызван/start')
    text='Вызван/start'
    print(text)
    update.message.reply_text(text)

def main():
    mybot=Updater("694246817:AAGK5kbmRcMbk2nTb_FcAAXorJr7qYbhNWE", request_kwargs=PROXY)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
    
main()