from rosebot import BOT, LOGS
from pyrogram import Filters, Message
import re

nfc = -1001486588099
arabian = re.compile('[\u0627-\u064a]')


@BOT.on_message(Filters.new_chat_members & Filters.chat(nfc))
def greet_new_users(bot: BOT, message: Message):
    new = message.new_chat_members
    for user in new:
        if arabian.search(user.first_name):
            BOT.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=0)
            BOT.send_message(message.chat.id, "arabian characters detected in name, user kicked from the chat")
        else:
            BOT.send_photo(nfc, "AgADBAAD0bExG9D-CVDg8aFwJMFwJ3gC", reply_to_message_id=message.message_id)