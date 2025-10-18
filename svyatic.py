import random

import telebot

BOT_TOKEN = '6817890701:AAFvaqFYn5T_YvF367VVwRDsqIwLV9BbYkE'

bot = telebot.TeleBot(BOT_TOKEN)

bul = ["Буль.", "Буль!", "Буль... Буль?", "Буль. Буль. Буль.", "Бууууль..."]


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if "святик" in str(message.text).lower():
        bot.reply_to(message, bul[random.randint(0, len(bul)-1)])


print(random.randint(0, len(bul) - 1))
bot.infinity_polling()
