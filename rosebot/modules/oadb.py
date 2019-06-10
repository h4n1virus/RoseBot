import requests

from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck


def oadb(artist):
    r = requests.get(
        "http://theaudiodb.com/api/v1/json/1/search.php?s={}".format(artist)
    )
    if r.status_code == 200:
        a = r.json()["artists"][0]
        text = "**{}**\n\n**Founded:** {}\n**Location:** {}\n**Genre:** {}\n**Mood:** {}\n\n{}".format(
            a["strArtist"],
            a["intFormedYear"],
            a["strCountry"],
            a["strGenre"],
            a["strMood"],
            a["strBiographyEN"],
        )
        return text, a["strArtistThumb"]


@BOT.on_message(Filters.command("oadb", "!"))
def post_oadb(bot: BOT, message: Message):
    message_text = message.text.replace("!oadb ", "")
    data = oadb(message_text)
    BOT.send_message(
        chat_id=message.chat_id,
        text=data[0],
        disable_notification=True,
        reply_to_message_id=ReplyCheck(message),
    )
    
    BOT.send_photo(
        chat_id=message.chat.id,
        photo=data[1],
        disable_notification=True,
    )
    if message.from_user.is_self:
        message.delete()