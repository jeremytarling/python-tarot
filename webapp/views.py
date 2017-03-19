# for the app routes
from webapp import app 
from flask import render_template


# for the cards 
from webapp import cards
# and the shuffle
import random


# home page
@app.route('/')
def index():
	return render_template("index.html")


# get one card
@app.route('/one-card')
def one_card():
	my_deck = cards.get_deck()
	my_card = cards.get_cards(my_deck)
	return render_template("one_card.html",
							name = my_card['name'],
							desc = my_card['desc'],
							image = my_card['image'])


# get three cards
@app.route('/three-cards')
def more_cards():
	my_deck = cards.get_deck()
	hand = []
	num = 1
	while num < 4:
		my_card = cards.get_cards(my_deck)
		hand.append(my_card)
		num +=1
	return render_template("three_cards.html", hand = hand)