from deck import Deck 

class Player:

    def __init__(self,name,coins,cards_self,cards_shown):
        self.name = name
        self.coins = coins
        self.cards_self = cards_self
        self.cards_shown = cards_shown

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):   
        self.__name = name
    
    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self,coins):
        if coins >= 0:
            self.__coins = coins
        else:
            self.__coins = 0

    @property
    def cards_self(self):
        return self.__cards_self

    @cards_self.setter
    def cards_self(self, cards_self):
        self.__cards_self = cards_self

    @property
    def cards_shown(self):
        return self.__cards_shown

    @cards_shown.setter
    def cards_shown(self, cards_shown):
        self.__cards_shown = cards_shown

    
    