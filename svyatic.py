import random

import telebot

BOT_TOKEN = '6817890701:AAFvaqFYn5T_YvF367VVwRDsqIwLV9BbYkE'

bot = telebot.TeleBot(BOT_TOKEN)

bul = ["Буль.", "Буль!", "Буль... Буль?", "Буль. Буль. Буль.", "Бууууль..."]


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if "Святик" in message.text:
        bot.reply_to(message, bul[random.randint(0, len(bul))])


print(random.randint(0, len(bul)))
bot.infinity_polling()
