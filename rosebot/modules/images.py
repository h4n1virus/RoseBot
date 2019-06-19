import os
import random
import requests
import re

from pyrogram import Filters, Message
from rosebot.helpers import ReplyCheck

from rosebot import BOT, FILEIDS_DIR


def create_lists(file_location):
    gifs = []
    videos = []
    photos = []
    for line in open(file_location):
        d = line.split('\t')
        file_id = d[1].split('\n')[0]
        if 'gif' in d[0]:
            gifs.append(file_id)
        elif 'video' in d[0]:
            videos.append(file_id)
        elif 'photo' in d[0]:
            photos.append(file_id)
    return gifs, videos, photos


def create_dictionary(file_ids_dir):
    dictionary = {}
    for file in os.listdir(file_ids_dir):
        file_location = "{}/{}".format(file_ids_dir, file)
        dict_name = os.path.splitext(file)[0]
        dictionary[dict_name] = {}
        gifs, videos, photos = create_lists(file_location)
        dictionary[dict_name]['gif'] = gifs
        dictionary[dict_name]['video'] = videos
        dictionary[dict_name]['photo'] = photos
    return dictionary

d = create_dictionary(FILEIDS_DIR)

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
        image = random.choice(d['rose_file_ids']['gif'])
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
        image = random.choice(d['rose_file_ids']['photo'])
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True, reply_to_message_id=ReplyCheck(message))
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(Filters.regex("(?i)(brexit|farage|nigel)"))
def post_brexit(bot: BOT, message: Message):
    image = random.choice(d['farage_file_ids']['photo'])
    BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)


@BOT.on_message(Filters.regex("(?i)(post|get|send) (drumpf|trump|orange man)"))
def post_trump(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (drumpf|trump|orange man)", message.text):
        image = random.choice(d['drump_file_ids']['photo'])
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
        image = random.choice(d['swift_file_ids']['photo'])
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
        image = random.choice(d['emma_file_ids']['photo'])
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(
    Filters.regex("(?i)(post|get|send) (sminem|smnem|smn|big ear (kid|guy)|chromosome)")
)
def post_sminem(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (sminem|smnem|smn|big ear (kid|guy)|chromosome)", message.text):
        image = random.choice(d['sminem_file_ids']['photo'])
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()


@BOT.on_message(Filters.regex("(?i)(post|get|send) (merchant|jew|rabbi)"))
def post_merchant(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (merchant|jew|rabbi)", message.text):
        if random.randint(1, 4) == 1:
            image = random.choice(d['merchant_file_ids']['gif'])
            BOT.send_animation(
                chat_id=message.chat.id,
                animation=image,
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message),
            )
        else:
            image = random.choice(d['merchant_file_ids']['photo'])
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
        if random.randint(1, 4) == 1:
            image = random.choice(d['gentoo_file_ids']['gif'])
            BOT.send_animation(
                chat_id=message.chat.id,
                animation=image,
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message),
            )
        else:
            image = random.choice(d['gentoo_file_ids']['photo'])
            BOT.send_photo(
                chat_id=message.chat.id,
                photo=image,
                disable_notification=True,
                reply_to_message_id=ReplyCheck(message),
            )


@BOT.on_message(Filters.regex("(?i)(post|get|send) (redpill|meme|maymay)"))
def post_redpill(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (redpill|meme|maymay)", message.text):
        image = random.choice(d['redpill_file_ids']['photo'])
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
        image = random.choice(d['911_file_ids']['photo'])
        BOT.send_photo(chat_id=message.chat.id, photo=image, disable_notification=True)
        if message.from_user.is_self:
            message.delete()


