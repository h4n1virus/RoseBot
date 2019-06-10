import requests

from pyrogram import Filters, Message

from rosebot import BOT, THECATAPI
from rosebot.helpers import ReplyCheck


def get_kot(mime_types):
    headers = {"x-api-key": THECATAPI}
    r = requests.get(
        "https://api.thecatapi.com/v1/images/search?mime_types={}".format(mime_types),
        headers=headers,
    )
    if r.status_code == 200:
        data = r.json()
        url = data[0]["url"]
        return url


@BOT.on_message(
    Filters.regex("(?i)(post|get|send) (kot|kots|cat|cats|🐱|🐈|😸|🐱) (gif|gifs)")
)
def post_kot_gif(bot: BOT, message: Message):
    kot_gif = get_kot(mime_types="gif")
    BOT.send_animation(
        chat_id=message.chat.id,
        animation=kot_gif,
        reply_to_message_id=ReplyCheck(message),
        disable_notification=True,
    )
    if message.from_user.is_self:
        message.delete()


@BOT.on_message(Filters.regex("(?i)(post|get|send) (kot|kots|cat|cats|🐱|🐈|😸|🐱)"))
def post_kot(bot: BOT, message: Message):
    kot_link = get_kot(mime_types="jpg,png")
    BOT.send_photo(
        chat_id=message.chat.id,
        photo=kot_link,
        reply_to_message_id=ReplyCheck(message),
        disable_notification=True,
    )
    if message.from_user.is_self:
        message.delete()
