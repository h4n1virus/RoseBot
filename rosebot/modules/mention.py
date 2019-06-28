from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck

@BOT.on_message(Filters.me & Filters.command('m', '.'))
def mention_everyone(bot: BOT, message: Message):
    bot.send_message(message.chat.id,
    message.command + "".join("[\u200E](tg://user?id={})".format(x.user.id) for x in bot.iter_chat_members(message.chat.id)),
    reply_to_message_id=ReplyCheck(message))