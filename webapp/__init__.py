from flask import Flask, render_template  # type: ignore
from .deck import draw, get_card
import json

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
    with open("webapp/static/json/reading-list.json", encoding="utf8") as file:
        selections = json.load(file)
    return render_template("reading_list.html", selections=selections)


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
    return render_template(
        "specific_card.html",
        card=this_card,
        previous_card=previous_card,
        next_card=next_card,
    )
