# for the app routes
from webapp import app 

# for the cards 
from webapp import cards
# and the shuffle
import random


# home page
@app.route('/')
def index():
	return "Hello World!"


# pick card(s) - call this method multiple times to draw multiple unique cards from the deck
def get_card(deck) :
	card = random.randint(1, len(deck))
	print(deck[card]['name'])
	print(deck[card]['desc'])
	del(deck[card]) # so we don't get the same card twice


# debug code
i = 1
while i < 4 :
	print("card " + str(i) + ":")
	my_deck = cards.get_deck()
	get_card(my_deck)
	print()
	i += 1

