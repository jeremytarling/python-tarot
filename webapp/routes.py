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


# tarot study
@app.route('/tarot-study', strict_slashes=False)
def all_cards():
	return render_template("tarot_study.html")

# reading list
@app.route('/reading-list', strict_slashes=False)
def reading_list():
	return render_template("reading_list.html")


# get one card
@app.route('/one-card', strict_slashes=False)
def one_card():
	my_deck = cards.get_deck()
	my_card = cards.get_card(my_deck)

	if my_card[0]['cardtype'] == "major" :
		return render_template("one_card.html",
								name = my_card[0]['name'],
								title = my_card[0]['name'],
								rev = my_card[1],
								meaning = my_card[0]['desc'],
								message = my_card[0]['message'],
								reversed_meaning = my_card[0]['rdesc'],
								image = my_card[0]['image'],
								url = my_card[0]['url'],
								cardtype = my_card[0]['cardtype'])
	else:
		return render_template("one_card.html",
								name = my_card[0]['name'],
								title = my_card[0]['name'],
								rev = my_card[1],
								meaning = my_card[0]['desc'],
								reversed_meaning = my_card[0]['rdesc'],
								image = my_card[0]['image'],
								url = my_card[0]['url'],
								cardtype = my_card[0]['cardtype'])

# get three cards
@app.route('/three-cards', strict_slashes=False)
def more_cards():
	my_deck = cards.get_deck()
	hand = []
	num = 1
	while num < 4:
		my_card = cards.get_card(my_deck)
		hand.append(my_card)
		num +=1
	return render_template("three_cards.html", hand = hand, title="Three card spread")


# get specific card
@app.route('/one-card/<card_url>')
def specific_card(card_url):
	my_deck = cards.get_deck()
	my_card = list(filter(lambda my_card: my_card['url'] == card_url, my_deck))[0]
	if my_card['sequence'] > 1 :
		previous_card_url = '/one-card/' + list(filter(lambda previous_card: previous_card['sequence'] == (my_card['sequence'] -1), my_deck))[0]['url']
	else :
		previous_card_url = '/tarot-study'
	if my_card['sequence'] < 78 :
		next_card_url = '/one-card/' + list(filter(lambda next_card: next_card['sequence'] == (my_card['sequence'] +1), my_deck))[0]['url']
	else :
		next_card_url = '/tarot-study'
	if my_card['cardtype'] == "major" :
		return render_template("specific_card.html",
								name = my_card['name'],
								title = my_card['name'],
								meaning = my_card['desc'],
								message = my_card['message'],
							    reversed_meaning = my_card['rdesc'],
								occult_title = my_card['occult_title'],
								hebrew_letter = my_card['hebrew_letter'],
								qabalah=my_card['qabalah'],
								meditation=my_card['meditation'],
								image = my_card['image'],
							    previous = previous_card_url,
							    next = next_card_url,
							    sequence = my_card['sequence'],
							    cardtype = my_card['cardtype'])
	else: 
		return render_template("specific_card.html",
								name = my_card['name'],
								title = my_card['name'],
								meaning = my_card['desc'],
								reversed_meaning = my_card['rdesc'],
								occult_title = my_card['occult_title'],
								qabalah=my_card['qabalah'],
								image = my_card['image'],
							    previous = previous_card_url,
							    next = next_card_url,
							    sequence = my_card['sequence'],
							    cardtype = my_card['cardtype'])


