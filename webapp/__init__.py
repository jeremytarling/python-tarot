from flask import Flask, render_template  # type: ignore
from .deck import deck, draw, get_card

app = Flask(__name__)


# home page
@app.route("/")
def index():
    return render_template("index.html")



# get a spread
@app.route("/<card_count>-card-spread", strict_slashes=False)
def more_cards(card_count):
    card_count = int(card_count)
    if card_count > len(deck):
        print("Cannot draw more cards than are in the deck.")
        card_count = len(deck)
    elif card_count < 1:
        print("Cannot draw fewer than one card.")
        card_count = 1
    return render_template(
        "spread.html",
        hand=[draw() for _ in range(card_count)],
        title=f"{card_count} card spread",
    )


# get specific card
@app.route("/card/<card_index>")
def specific_card(card_index):
    this_card, previous_card, next_card = get_card(int(card_index))
    return render_template(
        "spread.html",
        hand=[(this_card, False)],
        title=this_card["name"],
        previous_card=previous_card,
        next_card=next_card,
    )

