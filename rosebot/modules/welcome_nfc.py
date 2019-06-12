from rosebot import BOT, LOGS
from pyrogram import Filters, Message

nfc = -1001486588099

@BOT.on_message(Filters.new_chat_members & Filters.chat(nfc))
def greet_new_users(bot: BOT, message: Message):
    bot.send_photo(nfc, "AgADBAAD0bExG9D-CVDg8aFwJMFwJ3gC")