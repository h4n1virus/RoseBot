import requests

from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck

def define_word_ud(word):
    def get_data(word):
        r = requests.get(
            "http://api.urbandictionary.com/v0/define?term={}".format(word)
        )
        if r.status_code == 200:
            data = r.json()
            return data

    def get_definitions(data):
        definitions = []
        for definition in data["list"]:
            definitions.append(
                "{}\t{}\t{}".format(definition["word"], definition["definition"], definition["example"])
            )
        return definitions

    def get_five_results(definitions):
        five_definitions = ""
        for i in range(5):
            definition = definitions[i].split("\t")
            word = definition[0]
            definition_ = definition[1]
            example = definition[2]
            five_definitions = "{}\n**{}**\n{}\n\nExample:\n{}\n\n".format(
                five_definitions, word, definition_, example
            )
        return five_definitions


    data = get_data(word)
    if not data:
        return "Found nothing on Urban Dictionary"
    else:
        definitions = get_definitions(data)
        five_definitions = get_five_results(definitions)
        return five_definitions


@BOT.on_message(Filters.command("ud", "!"))
def post_ud(bot: BOT, message: Message):
    message_text = message.text.replace("!ud ", "")
    text = define_word_ud(message_text)
    BOT.send_message(
        chat_id=message.chat.id,
        text=text[:4096],
        disable_notification=True,
        reply_to_message_id=ReplyCheck(message),
    )
    if text[4096:]:
        BOT.send_message(
            chat_id=message.chat.id,
            text=text[4096:],
            disable_notification=True
        )
    if message.from_user.is_self:
        message.delete()