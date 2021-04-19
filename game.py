from deck import Deck
from player import Player
from numpy import random 
deck = Deck.create_deck()
choices = ['1','2','3','4','5','6','7','s']

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
            cls.__show_coins(player,cls.__players)
            print("\nSelect your play:\n1)Income\n2)Foreign aid\n3)Coup\n4)Tax\n5)Assasinate \
            \n6)Exchange\n7)Steal")
            choice = input()

            while choice not in choices:
                print("\nInvalid choice")
                print("\nSelect your play:\n1)Income\n2)Foreign aid\n3)Coup\n4)Tax\n5)Assasinate \
                \n6)Exchange\n7)Steal")
                choice = input()
            print('')
            if choice == '1':
                print('Income')
            if choice == '2':
                print("Foreign")
            if choice == '3':
                print('Coup')
            if choice == '4':
                print('Tax')
            if choice == '5':
                print('Assasinate')
            if choice == '6':
                print('Exchange')
            if choice == '7':
                print('Steal')
            if choice == 's':
                break
            turn += 1




    @classmethod
    def __set_players(cls,number):
        for i in range(1, number + 1):
            print("Enter players",i,"name: ")
            name = input()
            cls.__players.append(Player(name,2,cls.__random_cards(deck)))

    @classmethod
    def __random_cards(cls,deck):
        i = 0
        cards = []
        for i in range(2):
            cards.append(deck[i])
            deck.pop(i)
        return cards

    @classmethod
    def __show_coins(cls,current,players):
        print("Your coins:",current.coins)
        print('')
        for other in players:
            if other.name == current.name:
                continue
            print(other.name,"coins:",other.coins)


