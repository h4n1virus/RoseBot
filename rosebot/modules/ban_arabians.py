from rosebot import BOT, LOGS
from pyrogram import Filters, Message
import re

nfc = -1001486588099
arabian = (
    "/[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|"
    "[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]/")


@BOT.on_message(Filters.new_chat_members & Filters.chat(nfc))
def restrict_arabian(bot: BOT, message: Message):
    for new_member in message.new_chat_members:
        if re.match(arabian, new_member.first_name):
            BOT.restrict_chat_member(
            chat_id = message.chat.id,
            user_id = new_member.id
        )

@BOT.on_message(Filters.chat(nfc) & Filters.regex(arabian))
def delete_arabian(bot: BOT, message: Message):
    message.delete()
    LOGS.info("Persian detected, message deleted")