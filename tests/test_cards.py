"""Tests for the card-drawing logic in webapp/cards.py.

Run from the project root with:  python -m pytest
"""
from webapp import cards


def test_reversal_is_true_or_false():
    """Every draw should be either upright or reversed - nothing else."""
    for _ in range(1000):
        deck = cards.get_deck()
        card, rev = cards.get_card(deck)
        assert rev in (True, False), f"unexpected reversal value: {rev!r}"


def test_reversal_is_roughly_fifty_fifty():
    """Over many draws, about half the cards should come up reversed."""
    draws = 10_000
    reversed_count = 0
    for _ in range(draws):
        deck = cards.get_deck()
        card, rev = cards.get_card(deck)
        if rev:
            reversed_count += 1

    proportion = reversed_count / draws
    # With 10,000 fair coin flips, landing outside 0.47-0.53 is
    # vanishingly unlikely, so this test won't fail by chance.
    assert 0.47 < proportion < 0.53, f"{proportion:.1%} of cards were reversed"


def test_no_duplicate_cards_in_a_spread():
    """Drawing three cards from one deck should give three different cards."""
    deck = cards.get_deck()
    hand = [cards.get_card(deck)[0]["name"] for _ in range(3)]
    assert len(set(hand)) == 3