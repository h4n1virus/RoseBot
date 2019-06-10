from pyrogram import Filters, Message

from rosebot import BOT


@BOT.on_message(Filters.me & Filters.regex("(?i)(tbh|idk|wdym)"))
def fix_ngr_spk(bot: BOT, message: Message):
    if "tbh" in message.text:
        message_text = message.text.replace("tbh", "to be honest")
    elif "idk" in message.text:
        message_text = message.text.replace("idk", "I don't know")
    elif "wdym" in message.text:
        message_text = message.text.replace("wdym", "what do you mean")

    BOT.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=message_text
    )
