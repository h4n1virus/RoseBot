import requests

from pyrogram import Filters, Message

from rosebot import BOT, OMDBAPIKEY
from rosebot.helpers import ReplyCheck


def get_omdb(tiitel):
    def search(movie):
        r = requests.get(
            "http://www.omdbapi.com/?apikey={}&s={}".format(OMDBAPIKEY, movie)
        )
        if r.status_code == 200:
            data = r.json()
            imdb_id = data["Search"][0]["imdbID"]
            return imdb_id

    def movie_data(id):
        r = requests.get(
            "http://www.omdbapi.com/?apikey={}&i={}".format(OMDBAPIKEY, imdb_id)
        )
        if r.status_code == 200:
            data = r.json()
            return data

    def get_ratings(movie_data):
        ratings = ""
        for rating in movie_data["Ratings"]:
            ratings = "{}\n{}: {}".format(ratings, rating["Source"], rating["Value"])
        return ratings

    imdb_id = search(tiitel)
    movie_data = movie_data(imdb_id)

    title = "Title: **{}**\n".format(movie_data["Title"])
    director = "Director: {}\n".format(movie_data["Director"])
    writer = "Writer: {}\n".format(movie_data["Writer"])
    year = "Year: {}\n".format(movie_data["Year"])
    language = "Language: {}\n".format(movie_data["Language"])
    country = "Country: {}\n".format(movie_data["Country"])
    release = "Released: {}\n".format(movie_data["Released"])
    runtime = "Runtime: {}\n".format(movie_data["Runtime"])
    genre = "Genre: {}\n".format(movie_data["Genre"])
    actors = "Actors: {}\n".format(movie_data["Actors"])
    plot = "Plot: {}\n".format(movie_data["Plot"])
    awards = "Awards: {}\n".format(movie_data["Awards"])
    ratings = "Ratings: {}\n".format(get_ratings(movie_data))
    text = "{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
        title,
        director,
        writer,
        year,
        language,
        country,
        release,
        runtime,
        genre,
        actors,
        plot,
        awards,
        ratings,
    )
    return text


@BOT.on_message(Filters.command("omdb", "!"))
def post_omdb(bot: BOT, message: Message):
    message_text = message.text.replace("!omdb ", "")
    text = get_omdb(message_text)
    BOT.send_message(
        chat_id=message.chat_id,
        text=text,
        disable_notification=True,
        reply_to_message_id=ReplyCheck(message),
    )
    if message.from_user.is_self:
        message.delete()
