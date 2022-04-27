import os
import signal
import telebot
from flask import Flask
from buzz import generator
from modules import g_cal

bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))
app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    content = generator.generate_buzz() + '\n'
    content += g_cal.get_incomig_events()
    
    bot.send_message(os.getenv('TELEGRAM_CHANNEL_ID'), buzz)
    
    page = '<html><body><h1>'
    page += buzz
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
