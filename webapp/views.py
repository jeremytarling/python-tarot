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
	return "Hello World!"


# get one card
@app.route('/one-card')
def one_card():
	my_deck = cards.get_deck()
	my_card = cards.get_card(my_deck)
	return render_template("one_card.html",
							name = my_card['name'],
							desc = my_card['desc'],
							image = my_card['image'])


# get one card
@app.route('/three-cards')
def three_cards():
	return render_template("three_cards.html")