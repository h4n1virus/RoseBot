from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck

from mediawiki import MediaWiki

osrs = MediaWiki(url='https://oldschool.runescape.wiki/api.php')


def osrswiki(search_string):
    search = osrs.search(search_string)
    page = osrs.page(search[0])
    text = '**{}**\n\n{}\n**Read more at:** [{}]({})'.format(page.title, page.summary, page.title, page.url)
    return text


@BOT.on_message(Filters.command("osrswiki", "!"))
def wiki(bot: BOT, message: Message):
    topic = message.text.replace("!osrswiki ", "")
    summary = osrswiki(topic)

    BOT.send_message(
        chat_id=message.chat.id,
        text=summary,
        disable_notification=True,
        reply_to_message_id=ReplyCheck(message),
    )

    if message.from_user.is_self:
        message.delete()