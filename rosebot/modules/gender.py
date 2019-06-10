import requests

from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck


def genderize(first_name):
    r = requests.get("https://api.genderize.io/?name={}".format(first_name))
    if r.status_code == 200:
        try:
            a = r.json()
            text = "**Name:** {}\n**Gender:** {}\n**Probability:** {}".format(
                a["name"], a["gender"], a["probability"]
            )
            return text
        except KeyError:
            return


@BOT.on_message(Filters.regex("(?i)!gender"))
def gender(bot: BOT, message: Message):
    if message.reply_to_message is not None:
        first_name = message.reply_to_message.from_user.first_name
        message.reply(genderize(first_name))
        BOT.send_message(
            chat_id=message.chat.id,
            text=genderize(first_name),
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
    else:
        first_name = message.text.replace("!gender", "")
        BOT.send_message(
            chat_id=message.chat.id,
            text=genderize(first_name),
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
