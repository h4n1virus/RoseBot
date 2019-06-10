import requests
import random

from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck


def random_xkcd():
    r = requests.get("http://xkcd.com/{}/info.0.json".format(random.randint(1, 2156)))
    if r.status_code == 200:
        data = r.json()
        url = data["img"]
        return url


@BOT.on_message(Filters.command("xkcd", "!"))
def post_xkcd(bot: BOT, message: Message):
    BOT.send_photo(
        chat_id=message.chat.id,
        photo=random_xkcd(),
        reply_to_message_id=ReplyCheck(message),
        disable_notification=True,
    )

    if message.from_user.is_self:
        message.delete()
