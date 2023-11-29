import telebot
from env import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.chat.id, 'Hello , my name is Robomat , and Im ready to help you')

bot.polling()
