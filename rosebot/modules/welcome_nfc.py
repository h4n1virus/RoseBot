from rosebot import BOT, LOGS
from pyrogram import Filters, Message
import re

nfc = -1001486588099
arabian = (
    "/[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|"
    "[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]/")

@BOT.on_message(Filters.new_chat_members & Filters.chat(nfc))
def greet_new_users(bot: BOT, message: Message):
    new = message.new_chat_members
    for user in new:
        if re.search(arabian, user.first_name):
            BOT.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=0)
            BOT.unban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id)
            BOT.send_message(message.chat.id, "arabian characters detected in name, user kicked from the chat")
    bot.send_photo(nfc, "AgADBAAD0bExG9D-CVDg8aFwJMFwJ3gC")