import telebot
import os
from flask import Flask
import threading

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    bot.infinity_polling()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Money AI Bot is running!")

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
