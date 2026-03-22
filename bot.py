import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN not found")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_cmd(message):
    bot.reply_to(message, "မင်္ဂလာပါ")


@bot.message_handler(content_types=["new_chat_members"])
def welcome_new_members(message):
    for user in message.new_chat_members:
        name = user.first_name or "No Name"
        username = f"@{user.username}" if user.username else "No Username"

        text = (
            "Max Diamond Reseller ကနေ ကြိုဆိုပါတယ်\n\n"
            f"👤 Name - {name}\n"
            f"🆔 User ID - {user.id}\n"
            f"ℹ️ User Name - {username}"
        )

        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=["left_chat_member"])
def goodbye_member(message):
    user = message.left_chat_member
    name = user.first_name or "No Name"
    username = f"@{user.username}" if user.username else "No Username"

    text = (
        "ByeBye\n\n"
        f"👤 Name - {name}\n"
        f"🆔 User ID - {user.id}\n"
        f"ℹ️ User Name - {username}"
    )

    bot.send_message(message.chat.id, text)


print("Bot running...")
bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)။
