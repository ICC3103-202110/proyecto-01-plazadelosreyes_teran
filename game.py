from deck import Deck
from player import Player
from numpy import random
from logic import Logic

deck = Deck.create_deck()
choices = ['1','2','3','4','5','6','7','s']
players = []
class Game:

    p = str(input("Select number of players(3-4): "))
    while p != '3' and p != '4':
        print("Invalid number, try again")
        p = str(input("Select number of players(3-4): "))
    __number_of_players = int(p)

    @classmethod
    def play(cls):
        cls.__set_players(cls.__number_of_players)
        turn = 0
        while True:
            if turn > cls.__number_of_players-1:
                turn = 0
            player = players[turn]
            print('')

            print(player.name,"your turn:")
            print("Your cards:",player.cards)
            cls.__show_coins(player,players)

            choice =  cls.__turn(player)
            print('')
            if choice == '1':
                print(player.name,'chooses Income!')
                player.coins += 1
            if choice == '2':
                print(player.name,"chooses Foreign Aid!")
                if Logic.foreign_aid(player, players):
                    player.coins += 2
            if choice == '3':
                print(player.name,'chooses Coup!')
                Logic.coup(player, players)
            if choice == '4':
                print(player.name,'chooses Tax!')
            if choice == '5':
                print(player.name,'chooses Assasinate!')
            if choice == '6':
                print(player.name,'chooses Exchange!')
            if choice == '7':
                print(player.name,'chooses Steal!')
            if choice == 's':
                break
            turn += 1


    @classmethod
    def __set_players(cls,number):
        for i in range(1, number + 1):
            print("Enter players",i,"name: ")
            name = input()
            players.append(Player(name,2,cls.__random_cards(deck)))

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


    @classmethod
    def __turn(cls,current):

        print("\nSelect your play:\n1)Income\n2)Foreign aid\n3)Coup\n4)Tax\n5)Assasinate \
            \n6)Exchange\n7)Steal")
        if current.coins >= 10:
            print('You have 10+ coins, you can only play coup')
            choice = '3'
            return choice
        else:
            choice = input()

        if choice not in choices:
            print("\nInvalid choice")
            return cls.__turn(current)
        if choice == '3' and current.coins < 7:
            print('\nYou dont have enought coins to play Coup')
            return cls.__turn(current)
        if choice == '5' and current.coins < 3:
            print('\nYou dont have enought coins to play Assasination')
            return cls.__turn(current)
        
        return choice
        
        print('')

   



