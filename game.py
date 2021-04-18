from deck import Deck
from player import Player
from numpy import random 
deck = Deck.create_deck()

class Game:

    __players = []
    p = str(input("Insert number of players(3-4): "))
    while p != '3' and p != '4':
        print("Wrong number, try again")
        p = str(input("Insert number of players(3-4): "))
    __number_of_players = int(p)

    @classmethod
    def play(cls):
        cls.__set_players(cls.__number_of_players)
        turn = 0
        while True:
            if turn > cls.__number_of_players-1:
                turn = 0
            player = cls.__players[turn]
            print('')
            print(player.name,"your turn:")
            print("Your cards:",player.cards)
            print("Your coins:",player.coins)
            print("\nSelect your play:\n1)Income\n2)Foreign aid\n3)Coup\n4)Tax\n5)Assasinate \
            \n6)Exchange\n7)Steal")
            choice = input()
            if choice == 's':
                break
            turn += 1




    @classmethod
    def __set_players(cls,number):
        for i in range(1, number + 1):
            print("Enter players",i,"name: ")
            name = input()
            cls.__players.append(Player(name,0,cls.__random_cards(deck)))

    @classmethod
    def __random_cards(cls,deck):
        i = 0
        cards = []
        for i in range(2):
            cards.append(deck[i])
            deck.pop(i)
        return cards



