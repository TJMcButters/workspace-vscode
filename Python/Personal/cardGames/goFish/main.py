import random


def create_deck():
    value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suit = ['D', 'H', 'C', 'S']
    deck = []
    for v in value:
        for s in suit:
