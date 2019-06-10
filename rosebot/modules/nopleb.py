from pyrogram import Filters, Message

from rosebot import BOT

cbeats = [-1001105594526, -1001082868184]


@BOT.on_message(Filters.regex("banned for spam!") & Filters.chat(cbeats))
def delete_spam(bot: BOT, message: Message):
    message.delete()
