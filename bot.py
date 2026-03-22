import os
from datetime import datetime
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN not found")

bot = telebot.TeleBot(TOKEN)


def get_name(user):
    return user.first_name or "No Name"


def get_username(user):
    return f"@{user.username}" if user.username else "No Username"


def user_card(user):
    now = datetime.now()
    date_text = now.strftime("%d/%m/%Y")
    time_text = now.strftime("%I:%M:%S %p")
    return (
        f"👤 Name - {get_name(user)}\n"
        f"🆔 User ID - {user.id}\n"
        f"ℹ️ User Name - {get_username(user)}\n"
        f"🗓 Date - {date_text}\n"
        f"⏳ Time - {time_text}"
    )


@bot.message_handler(commands=["start"])
def start_cmd(message):
    bot.reply_to(message, "မင်္ဂလာပါ")


@bot.message_handler(content_types=["new_chat_members"])
def welcome_new_members(message):
    for user in message.new_chat_members:
        text = (
            f"PANDA Uc Resellerကနေ ကြိုဆိုပါတယ် owner နဲ့\n"
            f"Admin တို့မှာ Gift card များစွာရှိပါတယ်\n\n"
            f"Gpထဲ Ownerနဲ့ Admin သားရေးခွင့်ရှိပါတယ် gpထဲ\n"
            f"ရေးခွင့်မရှိတာ အမိန့်မပြုဘဲ Banပါမယ် !!!!\n\n"
            f"{user_card(user)}"
        )
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=["left_chat_member"])
def goodbye_member(message):
    user = message.left_chat_member
    text = (
        f"ဒီရင်ကာထွက်သွားပီနောက်လူဝင်မပျော်ရင်ပါ\n"
        f"နေ @{user.username if user.username else get_name(user)} နောက်လာလို့မရတော့\n"
        f"နေ ByeBye\n\n"
        f"{user_card(user)}"
    )
    bot.send_message(message.chat.id, text)


print("Bot running...")
bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)
