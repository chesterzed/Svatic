import random
import requests
import json
import telebot

BOT_TOKEN = '6817890701:AAFvaqFYn5T_YvF367VVwRDsqIwLV9BbYkE'

bot = telebot.TeleBot(BOT_TOKEN)

bul = ["Буль.", "Буль!", "Буль... Буль?", "Буль. Буль. Буль.", "Бууууль..."]


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if "святик" in str(message.text).lower():
        bot.reply_to(message, bul[random.randint(0, len(bul)-1)])
    if "святослав" in str(message.text).lower():
        data = 'Буль'
        try:
            response = requests.get('https://api.quotable.io/random')
            if response.status_code == 200:
                data = response.json()
                data = f"{data['content']}\n\t\t- {data['author']}"
        except:
            data = bul[random.randint(0, len(bul) - 1)]


        bot.reply_to(message, data)



print(random.randint(0, len(bul) - 1))
bot.infinity_polling()
