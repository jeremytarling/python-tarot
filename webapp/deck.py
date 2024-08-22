import random
import json


# does what it says on the tin
def shuffle_deck(deck):
    random.shuffle(deck)


# pick card(s) - call this method multiple times to draw multiple unique cards from the deck
def get_card(deck):
    num = random.randint(0, len(deck) - 1)  # the minus 1 fixes the zero indexed array out-of-range error
    card = deck[num]
    del (deck[num])  # so we don't get the same card twice if we're calling this multiple times for the same hand
    rev = random.randint(-1, 1)  # is card reversed? zero (false) or 1 (true)
    drawn = (card, rev)  # tuple of card dictionary + 1 or zero for reversal
    return drawn


# array of dicts for each card
def get_deck():
    with open('deck.json', 'r') as file:
        deck = json.load(file)
    return deck
