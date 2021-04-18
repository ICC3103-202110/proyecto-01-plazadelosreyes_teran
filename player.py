class Player:

    def __init__(self,name,coins,cards):
        self.name = names
        self.coins = coins
        self.cards = []

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
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = cards
    