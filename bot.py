import telebot
import telebot.util
import telebot.types
import config
import random
from time import sleep

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> бот, введи текс и я отправлюего в будущее".format(message.from_user, bot.get_me()), parse_mode='html')
    

@bot.message_handler(content_types=['text'])
def delorian(message):
    text_time = message.text
    how_time = random.randint(1000, 10000)
    bot.send_message(message.chat.id, "сообщение было отправленно в будущее на {} секунд".format(how_time))
    sleep(how_time)
    bot.send_message(message.chat.id, text_time)

            
bot.polling(none_stop=True)