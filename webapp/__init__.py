from flask import Flask, render_template  # type: ignore
from .deck import draw, get_card

app = Flask(__name__)


# home page
@app.route("/")
def index():
    return render_template("index.html")


# tarot study
@app.route("/tarot-study", strict_slashes=False)
def all_cards():
    return render_template("tarot_study.html")


# reading list
@app.route("/reading-list", strict_slashes=False)
def reading_list():
    return render_template("reading_list.html")


# get one card
@app.route("/one-card", strict_slashes=False)
def one_card():
    this_card, is_reversed = draw()
    return render_template(
        "one_card.html",
        card=this_card,
        is_reversed=is_reversed,
    )


# get three cards
@app.route("/three-cards", strict_slashes=False)
def more_cards():
    hand = [draw() for _ in range(3)]
    return render_template("three_cards.html", hand=hand, title="Three card spread")


# get specific card
@app.route("/one-card/<card_url>")
def specific_card(card_url):
    this_card, previous_card, next_card = get_card(card_url)
    is_major = this_card["card_type"] == "major"

    return render_template(
        "specific_card.html",
        name=this_card["name"],
        title=this_card["name"],
        meaning=this_card["desc"],
        message=this_card["message"] if is_major else None,
        reversed_meaning=this_card["rdesc"],
        hebrew_letter=this_card["hebrew_letter"] if is_major else None,
        qabalah=this_card["qabalah"],
        meditation=this_card["meditation"] if is_major else None,
        image=this_card["image"],
        previous=previous_card["url"] if previous_card else "/tarot-study",
        next=next_card["url"] if next_card else "/tarot-study",
        sequence=this_card["sequence"],
        card_type=this_card["card_type"],
    )
