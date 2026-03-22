import os
from datetime import datetime
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN not found")

bot = telebot.TeleBot(TOKEN)


def format_user_text(user):
    name = user.first_name or "No Name"
    user_id = user.id
    username = f"@{user.username}" if user.username else "No Username"
    now = datetime.now()

    date_text = now.strftime("%d/%m/%Y")
    time_text = now.strftime("%I:%M:%S %p")

    text = (
        f"👤 Name - {name}\n"
        f"🆔 User ID - {user_id}\n"
        f"ℹ️ User Name - {username}\n"
        f"🗓 Date - {date_text}\n"
        f"⏳ Time - {time_text}"
    )
    return text


@bot.message_handler(content_types=["new_chat_members"])
def welcome_new_members(message):
    for user in message.new_chat_members:
        name = user.first_name or "bro"
        username = f"@{user.username}" if user.username else name

        caption = (
            f"🌸 မင်္ဂလာပါ {username}\n\n"
            f"ဒီ Group ထဲကို ဝင်လာတဲ့အတွက် ကြိုဆိုပါတယ်။\n"
            f"စည်းကမ်းချက်တွေကို လိုက်နာပေးပါ။\n\n"
            f"{format_user_text(user)}"
        )

        bot.send_message(message.chat.id, caption)


@bot.message_handler(content_types=["left_chat_member"])
def goodbye_member(message):
    user = message.left_chat_member
    name = user.first_name or "bro"
    username = f"@{user.username}" if user.username else name

    caption = (
        f"👋 ByeBye {username}\n\n"
        f"Group ထဲမှ ထွက်သွားပါပြီbyebye par။\n\n"
        f"{format_user_text(user)}"
    )

    bot.send_message(message.chat.id, caption)


print("Bot running...")
bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)
