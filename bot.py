import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN not found")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Bot အလုပ်လုပ်နေပြီ ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"နင်ရေးတာ: {message.text}")

print("Bot started...")
bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)
