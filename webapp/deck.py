import random
import json

arcana_labels = {
    "major": "",
    "wands": "wa",
    "cups": "cu",
    "swords": "sw",
    "pentacles": "pe",
    "coins": "pe",
}

person_labels = {
    "king": "ki",
    "queen": "qu",
    "knight": "kn",
    "page": "pa",
}

def get_image(card):
    suit_label = arcana_labels[card["suit"]]
    if isinstance(card["rank"], int):
        rank_label = str(card["rank"]).zfill(2)
    else:
        rank_label = person_labels[card["rank"]]
    return f"images/{suit_label}{rank_label}.jpeg"

def draw():
    card = random.choice(deck)
    is_reversed = random.choice([True, False])
    return (card, is_reversed)


def get_card(card_index):
    this_card = None
    previous_card = None
    next_card = None

    if card_index <= 0 and card_index >= len(deck):
        raise ValueError("This card is not in the deck")

    this_card = deck[card_index]
    if card_index > 0:
        previous_card = deck[card_index - 1]
    if card_index < len(deck) - 1:
        next_card = deck[card_index + 1]

    return (this_card, previous_card, next_card)


with open("webapp/static/json/cards.json", encoding="utf8") as file:
    deck = json.load(file)
for card in deck:
    card["index"] = deck.index(card)
    card["image"] = get_image(card)
