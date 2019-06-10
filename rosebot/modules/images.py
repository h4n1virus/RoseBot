import os
import random
import requests
import re

from pyrogram import Filters, Message
from rosebot.helpers import ReplyCheck

from rosebot import (
    BOT,
    ROSE_DIR,
    ROSE_GIF_DIR,
    FARAGE_DIR,
    TRUMP_DIR,
    WATSON_DIR,
    SWIFT_DIR,
    SMINEM_DIR,
    MERCHANT_DIR,
    REDPILL_DIR,
    NINE_ELEVEN_DIR,
    GENTOO_DIR,
)


def get_random_image(directory):
    random_picture = random.choice(os.listdir(directory))
    path_to_picture = os.path.join(directory, random_picture)
    if os.path.isfile(path_to_picture):
        return path_to_picture


def drumpf_quote():
    r = requests.get("https://api.tronalddump.io/random/quote")
    if r.status_code == 200:
        a = r.json()
        text = "**{}**\n\n{}".format(a["value"], a["_embedded"]["source"][0]["url"])
        return text


@BOT.on_message(
    Filters.regex(
        "(?i)(post|get|send) (rose|indigo girl|blue girl|love|roze|crush|🌹) (gif|gifs)"
    )
)
def post_rose_gif(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (rose|indigo girl|blue girl|love|roze|crush|🌹) (gif|gifs)", message.text):
        image = get_random_image(ROSE_GIF_DIR)
        BOT.send_animation(
            chat_id=message.chat.id, animation=image, disable_notification=True, reply_to_message_id=ReplyCheck(message)
        )
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(
    Filters.regex("(?i)(post|get|send) (rose|indigo girl|blue girl|love|roze|crush|🌹)")
)
def post_rose(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (rose|indigo girl|blue girl|love|roze|crush|🌹)", message.text):
        image = get_random_image(ROSE_DIR)
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True, reply_to_message_id=ReplyCheck(message))
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(Filters.regex("(?i)(brexit|farage|nigel)"))
def post_brexit(bot: BOT, message: Message):
    image = get_random_image(FARAGE_DIR)
    BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)


@BOT.on_message(Filters.regex("(?i)(post|get|send) (drumpf|trump|orange man)"))
def post_trump(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (drumpf|trump|orange man)", message.text):
        image = get_random_image(TRUMP_DIR)
        BOT.send_photo(
            chat_id=message.chat.id,
            photo=image,
            disable_notification=True,
            caption=drumpf_quote(),
        )
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(Filters.regex("(?i)(post|get|send) (tay|taytay|taylor|tswift|swift|trap)"))
def post_swift(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (tay|taytay|taylor|tswift|swift|trap)", message.text):
        image = get_random_image(SWIFT_DIR)
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()

@BOT.on_message(
    Filters.regex(
        "(?i)(post|get|send) (whore|slut|watson|emma|hermione|granger|harry potter girl)"
    )
)
def post_watson(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (whore|slut|watson|emma|hermione|granger|harry potter girl)", message.text):
        image = get_random_image(WATSON_DIR)
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(
    Filters.regex("(?i)(post|get|send) (sminem|smnem|smn|big ear (kid|guy)|chromosome)")
)
def post_sminem(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (sminem|smnem|smn|big ear (kid|guy)|chromosome)", message.text):
        image = get_random_image(SMINEM_DIR)
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(Filters.regex("(?i)(post|get|send) (merchant|jew|rabbi)"))
def post_merchant(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (merchant|jew|rabbi)", message.text):
        image = get_random_image(MERCHANT_DIR)
        if ".gif" in os.path.splitext(image):
            BOT.send_animation(
                chat_id=message.chat.id,
                animation=image,
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message),
            )
        else:
            BOT.send_photo(
                chat_id=message.chat.id,
                photo=image,
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message),
            )
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(Filters.regex("(?i)(post|install|get|send) (gentoo|linux)"))
def post_gentoo(bot: BOT, message: Message):
    if re.match("(?i)(post|install|get|send) (gentoo|linux)", message.text):
        image = get_random_image(GENTOO_DIR)
        if ".gif" in os.path.splitext(image):
            BOT.send_animation(
                chat_id=message.chat.id,
                animation=image,
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message),
            )
        else:
            BOT.send_photo(
                chat_id=message.chat.id,
                photo=image,
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message),
            )


@BOT.on_message(Filters.regex("(?i)(post|get|send) (redpill|meme|maymay)"))
def post_redpill(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (redpill|meme|maymay)", message.text):
        image = get_random_image(REDPILL_DIR)
        if ".gif" in os.path.splitext(image):
            BOT.send_animation(
                chat_id=message.chat.id, animation=image, disable_notification=True
            )
        else:
            BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(
    Filters.regex(
        "(?i)((post|get|send) (911|bush|twin towers|wtc)|bush did (911|9/11))"
    )
)
def post_911(bot: BOT, message: Message):
    if re.match("(?i)((post|get|send) (911|bush|twin towers|wtc)|bush did (911|9/11))", message.text):
        image = get_random_image(NINE_ELEVEN_DIR)
        if ".gif" in os.path.splitext(image):
            BOT.send_animation(
                chat_id=message.chat.id, animation=image, disable_notification=True
            )
        else:
            BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()
