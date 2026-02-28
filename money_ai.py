import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Money AI is live.")

@bot.message_handler(commands=['recover'])
def recover(message):
    bot.reply_to(message, "Send debtor objection after /recover")

@bot.message_handler(commands=['sales'])
def sales(message):
    bot.reply_to(message, "Send customer objection after /sales")

if __name__ == "__main__":
    bot.infinity_polling()
