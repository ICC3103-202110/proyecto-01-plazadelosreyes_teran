from deck import Deck
from player import Player
from numpy import random
from logic import Logic

deck = Deck.create_deck()
choices = ['1','2','3','4','5','6','7','s']
players = []
active_players = []
inactive_players = []

class Game:

    p = str(input("Select number of players(3-4): "))
    while p != '3' and p != '4':
        print("Invalid number, try again")
        p = str(input("Select number of players(3-4): "))

    __number_of_players = int(p)

    @classmethod
    def play(cls):
        turn = 0
        cls.__set_players(cls.__number_of_players)
        while True:
            if turn > cls.__number_of_players-1:
                turn = 0
            player = active_players[turn]
            print('')

            print(player.name,"your turn:")
            print("Your cards:",player.cards_self)
            print("Your coins:",player.coins)
            print('')
            print('Active players:')
            cls.__show_players(player,active_players)
            if len(inactive_players) > 0:
                print('\n,Inactive players:')
                cls.__show_players(player,inactive_players)
            choice =  cls.__turn(player)
            print('')
            if choice == '1':
                print(player.name,'chooses Income!')
                actual_coins = player.coins
                player.coins = actual_coins + 1
            if choice == '2':
                print(player.name,"chooses Foreign Aid!")
                if Logic.foreign_aid(player, active_players):
                    actual_coins = player.coins
                    player.coins = actual_coins + 2
            if choice == '3':
                print(player.name,'chooses Coup!')
                Logic.coup(player, active_players)
                actual_coins = player.coins
                player.coins = actual_coins - 7
            if choice == '4':
                print(player.name,'chooses Tax!')
                if Logic.tax(player, active_players):
                    actual_coins = player.coins
                    player.coins = actual_coins + 3
            if choice == '5':
                print(player.name,'chooses Assasinate!')
                if Logic.assasinate(player, active_players):
                    actual_coins = player.coins
                    player.coins = actual_coins - 3
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
            shown = ['*','*']
            print("Enter players",i,"name: ")
            name = input()
            cards = cls.__random_cards(deck)
            coins = 2
            players.append(Player(name,coins,cards,shown))
            active_players.append(Player(name,coins,cards,shown))

    @classmethod
    def __random_cards(cls,deck):
        i = 0
        cards = []
        for i in range(2):
            cards.append(deck[i])
            deck.pop(i)
        return cards

    @classmethod
    def __show_players(cls,current,players):
        for other in players:
            if other.name == current.name:
                continue
            print(other.name,"coins:",other.coins)
            print(other.name,'cards:',other.cards_shown)


    @classmethod
    def __turn(cls,current):
        print()
        print(current.name,"Select your play:\n1)Income\n2)Foreign aid\n3)Coup\n4)Tax\n5)Assasinate \
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
            print('\nYou dont have enough coins to play Coup')
            return cls.__turn(current)
        if choice == '5' and current.coins < 3:
            print('\nYou dont have enough coins to play Assasination')
            return cls.__turn(current)
        
        return choice
        
        print('')

   



