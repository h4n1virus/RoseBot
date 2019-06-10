import requests
import re

from rosebot import BOT

from pyrogram import Filters, Message


categories = [
    "explicit",
    "dev",
    "movie",
    "food",
    "celebrity",
    "science",
    "sport",
    "political",
    "religion",
    "animal",
    "history",
    "music",
    "travel",
    "career",
    "money",
    "fashion",
]


def match_word(string_list, string):
    for word in string_list:
        match = re.search(word, string)
        if match is not None:
            match = word
            break
        else:
            match = ""
    return match


def chuck_norris(message=""):
    category = match_word(categories, message)
    r = requests.get(
        "https://api.chucknorris.io/jokes/random?category={}".format(category)
    )
    if r.status_code == 200:
        a = r.json()
        return a["value"]


def jokes_with_punchline():
    r = requests.get("https://official-joke-api.appspot.com/jokes/random")
    if r.status_code == 200:
        a = r.json()
        text = "**{}**\n\n{}".format(a["setup"], a["punchline"])
        return text


@BOT.on_message(Filters.regex("(?i)chuck norris"))
def chuck_joke(bot: BOT, message: Message):
    message.reply(chuck_norris(message.text), disable_notification=True)


@BOT.on_message(Filters.regex("(?i)tell me a joke"))
def tell_joke(bot: BOT, message: Message):
    message.reply(jokes_with_punchline(), disable_notification=True)
