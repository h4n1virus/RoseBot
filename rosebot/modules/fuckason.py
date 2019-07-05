from time import sleep
from random import randint
from pyrogram import Filters, Message

from rosebot import BOT

sausage = [828947812, 63325928]
nfc = -1001486588099

@BOT.on_message(Filters.user(sausage) & Filters.chat(nfc))
def fuckthem(bot: BOT, message: Message):
    sleep(randint(2,6))
    message.delete()