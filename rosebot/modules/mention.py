from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck


@BOT.on_message(Filters.me & Filters.command('m', '.'))
def mention_everyone(bot: BOT, message: Message):
    mentions = "".join("[\u200E](tg://user?id={})".format(x.user.id) for x in BOT.iter_chat_members(message.chat.id))
    BOT.send_message(
    message.chat.id,
    message.text.replace('.m', ' ') + mentions[:4096],
    reply_to_message_id=ReplyCheck(message))
    message.delete()