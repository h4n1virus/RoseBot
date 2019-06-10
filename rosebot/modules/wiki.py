import requests

from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck


def wikipedia_summary(topic):
    r = requests.get(
        "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(topic)
    )
    if r.status_code == 200:
        data = r.json()
        text = "{}\n**Read more at:** [{}]({})".format(
            data["extract"], data["title"], data["content_urls"]["desktop"]["page"]
        )
        return text


@BOT.on_message(Filters.command("wiki", "!"))
def wiki(bot: BOT, message: Message):
    topic = message.text.replace("!wiki ", "")
    summary = wikipedia_summary(topic)

    BOT.send_message(
        chat_id=message.chat.id,
        text=summary,
        disable_notification=True,
        reply_to_message_id=ReplyCheck(message),
    )

    if message.from_user.is_self:
        message.delete()
