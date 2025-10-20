import random
import requests
import json
import telebot

BOT_TOKEN = '6817890701:AAFvaqFYn5T_YvF367VVwRDsqIwLV9BbYkE'
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# И используйте сессию с отключенной проверкой SSL
session = requests.Session()
session.verify = False
response = session.get('https://api.quotable.io/random', timeout=10)
print(response.json())


bot = telebot.TeleBot(BOT_TOKEN)

bul = ["Буль.", "Буль!", "Буль... Буль?", "Буль. Буль. Буль.", "Бууууль..."]


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if "святик" in str(message.text).lower():
        bot.reply_to(message, random.choice(bul))
    elif "святослав" in str(message.text).lower():
        try:
            response = requests.get('https://api.quotable.io/random', timeout=10)
            print(response)
            if response.status_code == 200:
                data = response.json()
                quote_text = f"{data['content']}\n\t\t- {data['author']}"
                bot.reply_to(message, quote_text)
        except:
            data = random.choice(bul)
            bot.reply_to(message, data)


print(random.randint(0, len(bul) - 1))
bot.infinity_polling(timeout=60)
