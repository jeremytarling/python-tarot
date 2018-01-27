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


# home page
@app.route('/all-cards')
def all_cards():
	return render_template("all_cards.html")


# get one card
@app.route('/one-card')
def one_card():
	my_deck = cards.get_deck()
	my_card = cards.get_cards(my_deck)
	return render_template("one_card.html",
							name = my_card[0]['name'],
							title = my_card[0]['name'],
							rev = my_card[1],
							meaning = my_card[0]['desc'],
							reversed_meaning = my_card[0]['rdesc'],
							image = my_card[0]['image'],
							url = my_card[0]['url'])


# get specific card
@app.route('/one-card/<card_url>')
def specific_card(card_url):
	my_deck = cards.get_deck()
	my_card = next((item for item in my_deck if item["url"] == card_url))
	return render_template("specific_card.html",
							name = my_card['name'],
							title = my_card['name'],
							meaning = my_card['desc'],
							reversed_meaning = my_card['rdesc'],
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
	return render_template("three_cards.html", hand = hand, title="Three card spread")




