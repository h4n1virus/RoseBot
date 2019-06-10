import requests

import detectlanguage

from pyrogram import Filters, Message

from rosebot import BOT, DETECTLANGUAGEAPI

detectlanguage.configuration.api_key = DETECTLANGUAGEAPI


def translate_neurotolge(text, fromlang="auto", to_lang=None):
    if "et" in to_lang:
        to_lang = "et"
    elif "en" in to_lang:
        to_lang = "en"
    elif "ru" in to_lang:
        to_lang = "ru"
    elif "lv" in to_lang:
        to_lang = "lv"
    else:
        langapi = detectlanguage.detect(text)[0]
        if "et" in langapi["language"]:
            to_lang = "en"
        elif "ru" in langapi["language"]:
            to_lang = "en"
        elif "lv" in langapi["language"]:
            to_lang = "en"
        elif "en" in langapi["language"]:
            to_lang = "et"

    r = requests.get(
        "https://neurotolge.ee/translate?from={}&to={}&q={}".format(
            fromlang, to_lang, text
        ),
        verify=False,
    )
    if r.status_code == 200:
        a = r.json()
        translation = a["translations"][0]["translation"]
        return translation


@BOT.on_message(Filters.command("Tõlgi", "!"))
def translate_message(bot: BOT, message: Message):
    if message.reply_to_message is not None:
        tolang = message.text[-2:]
        if "et" in tolang:
            tolang = "et"
        elif "en" in tolang:
            tolang = "en"
        elif "ru" in tolang:
            tolang = "ru"
        elif "lv" in tolang:
            tolang = "lv"
        else:
            tolang = ""
        replied_message = message.reply_to_message.text
        translated_text = translate_neurotolge(replied_message, to_lang=tolang)
        BOT.send_message(
            chat_id=message.chat.id,
            text=translated_text,
            disable_notification=True,
            reply_to_message_id=message.reply_to_message.message_id,
        )
