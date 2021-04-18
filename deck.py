from numpy import random
from random import shuffle

class Deck:
    
    def create_deck():
        DECK = []
        for i in range(3):
            DECK.append('Duke')
            DECK.append('Assasin')
            DECK.append('Ambassador')
            DECK.append('Captain')
            DECK.append('Contessa')
        shuffle(DECK)
        return DECK


