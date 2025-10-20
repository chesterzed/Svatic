import random
import requests
import json
import telebot

BOT_TOKEN = '6817890701:AAFvaqFYn5T_YvF367VVwRDsqIwLV9BbYkE'
bot = telebot.TeleBot(BOT_TOKEN)

# response = requests.get('https://zenquotes.io/api/random', timeout=10)
# print(response)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     quote_text = f"{data[0]['q']}\n\t\t- {data[0]['a']}"
#     print(quote_text)

bul = ["Буль.", "Буль!", "Буль... Буль?", "Буль. Буль. Буль.", "Бууууль..."]


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    msg_txt = str(message.text).lower()

    if "святик" in msg_txt:
        bot.reply_to(message, random.choice(bul))
    elif "святослав" in msg_txt:
        try:
            response = requests.get('https://zenquotes.io/api/random', timeout=15)
            if response.status_code == 200:
                data = response.json()
                quote_text = f"{data[0]['q']}\n\t\t- {data[0]['a']}"
                bot.reply_to(message, quote_text)
        except:
            data = random.choice(bul)
            bot.reply_to(message, data)


bot.infinity_polling(timeout=60)
