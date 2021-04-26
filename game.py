from numpy import random
from deck import Deck
from player import Player
from logic import Logic

deck = Deck.create_deck()
choices = ['1','2','3','4','5','6','7','s']
players = []
active_players = []
inactive_players = []
names = []

class Game:

    print("░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓ Ⓒ                             ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░")
    print("░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓          Ⓞ                    ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░")
    print("░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓                   Ⓤ           ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░")
    print("░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓                            Ⓟ  ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░\n")

    p = str(input("Select the number of players(3-4): "))
    while p != '3' and p != '4':
        print("Invalid number, try again")
        p = str(input("Select the number of players(3-4): "))
    __number_of_players = int(p)

    @classmethod
    def play(cls,flag):
        if flag == 0:
            cls.__set_players(cls.__number_of_players)
        flag = 1
        while True:
            for current in players:
                if current.name not in names:
                    continue
                player = current
                print('')
                print(player.name,"it\'s your turn:")
                print(" -→ Cards:",player.cards_self)
                print(" -→ Coins:",player.coins)
                print('')
                print('Active players ♥ :')
                cls.__show_players(player,active_players)
                if len(inactive_players) > 0:
                    print('\nInactive players ☠ :')
                    cls.__show_players(player,inactive_players)
                choice =  cls.__turn(player)
                print('')
                if choice == '1':
                    print(player.name,'chooses Income!')
                    player.coins += 1
                if choice == '2':
                    print(player.name,"chooses Foreign Aid!")
                    if Logic.foreign_aid(player, active_players):
                        player.coins += 2
                if choice == '3':
                    print(player.name,'chooses Coup!')
                    Logic.coup(player, active_players)
                    player.coins -= 7
                if choice == '4':
                    print(player.name,'chooses Tax!')
                    if Logic.tax(player, active_players):
                        player.coins += 3
                if choice == '5':
                    print(player.name,'chooses Assasinate!')
                    if Logic.assasinate(player, active_players):
                        player.coins -= 3
                if choice == '6':
                    print(player.name,'chooses Exchange!')
                    Logic.exchange(player, active_players)
                if choice == '7':
                    print(player.name,'chooses Steal!')
                    if Logic.steal(player, active_players):
                        player.coins += 2
                cls.__remove_player()
                if cls.__declare_winner() != False:
                    return 0
            print("\n════════════════════════ END OF TURN ════════════════════════")

    @classmethod
    def __set_players(cls,number):
        for i in range(1, number + 1):
            shown = ['*','*']
            print("Enter player",i,"name: ")
            name = input()
            while name == "":
                print("Invalid name, try again")
                print("Enter player",i,"name: ")
                name = input()
            cards = cls.__random_cards(deck)
            coins = 2
            players.append(Player(name,coins,cards,shown))
            active_players.append(Player(name,coins,cards,shown))
            names.append(name)

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
            print(other.name,"-→ Coins:",other.coins, '  Cards:', other.cards_shown)

    @classmethod
    def __turn(cls,current):
        print()
        print(current.name,"Select the number of your play:\n1) ☞ Income\n2) ☞ Foreign aid\n3) ☞ Coup\n4) ☞ Tax\
            \n5) ☞ Assasinate\n6) ☞ Exchange\n7) ☞ Steal")
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
            print('\nYou don\'t have enough coins to play Coup')
            return cls.__turn(current)
        if choice == '5' and current.coins < 3:
            print('\nYou don\'t have enough coins to play Assasination')
            return cls.__turn(current)
        return choice
        print('')

    @classmethod
    def __remove_player(cls):
        for player in active_players:
            if len(player.cards_self) == 0:
                active_players.remove(player)
                inactive_players.append(player)
                names.remove(player.name)
                print()
                print(player.name,"is out of the game!")
    
    @classmethod
    def __declare_winner(cls):
        if len(active_players) == 1:
            winner = active_players[0]
            print("\nThe winner is", active_players[0].name,"!")
            return winner
        else:
            return False