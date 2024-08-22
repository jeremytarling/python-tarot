import random
import json

with open("webapp/static/json/cards.json", encoding="utf8") as file:
    deck = json.load(file)


def draw():
    card = random.choice(deck)
    is_reversed = random.choice([True, False])
    return (card, is_reversed)


def get_card(card_url):
    this_card = None
    previous_card = None
    next_card = None

    for i, card in enumerate(deck):
        if card["url"] == card_url:
            this_card = card
            if i > 0:
                previous_card = deck[i - 1]
            if i < len(deck) - 1:
                next_card = deck[i + 1]
            break

    return (this_card, previous_card, next_card)
