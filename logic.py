from numpy import random
from random import shuffle
from deck import Deck
from player import Player
deck = Deck.create_deck()

class Logic:

    def challenge(challenged,players,card):
        challengers = []
        for challenge in players:
            if challenged.name == challenge.name:
                continue
            print('')
            print(challenge.name,"your cards:",challenge.cards_self)
            print('Do you want to challenge',challenged.name,'(y/n):')
            r = input()
            if r == 'y':
                challengers.append(challenge)
        if len(challengers) > 0:
            if len(challengers) > 1:
                challenger = challengers[random.randint(0,len(challengers)-1)]
            if len(challengers) == 1:
                challenger = challengers[0]
            print('')
            print(challenger.name,'decides to challenge',challenged.name,'\n')
            if card == "Captain":
                cards = [card, "Ambassador"]
                for i in cards:
                    if i in challenged.cards_self:
                        challenged.cards_shown.remove('*')
                        challenged.cards_shown.append(i)
                        print(challenged.name,'cards:',challenged.cards_shown)
                        print(challenged.name,'has a',i+'!\n')
                        print(challenger.name,'you lost the challenge')
                        Logic.loose_card(challenger)
                        Logic.change_card(challenged, i)
                        return True
                    else:
                        print(challenged.name,'You don\'t have the',i)
                        Logic.loose_card(challenged)
                        return False
            else:            
                if card in challenged.cards_self:
                    challenged.cards_shown.remove('*')
                    challenged.cards_shown.append(card)
                    print(challenged.name,'cards:',challenged.cards_shown)
                    print(challenged.name,'has a',card+'!\n')
                    print(challenger.name,'you lost the challenge')
                    Logic.loose_card(challenger)
                    Logic.change_card(challenged, card)
                    return True
                else:
                    print(challenged.name,'You don\'t have the',card)
                    Logic.loose_card(challenged)
                    return False
        else: 
            print('\nNobody challenged',challenged.name)
            return 'no one'

    def counter(players,current):
        blockers = []
        for block in players:
            if current.name == block.name:
                continue
            print('')
            print(block.name,'your cards:',block.cards_self)
            print('Do you want to block',current.name,'(y/n)')
            r = input()
            if r == 'y':
                blockers.append(block)
        if len(blockers) > 0:
            if len(blockers) > 1:
                blocker = blockers[random.randint(0,len(blockers)-1)]
            if len(blockers) == 1:
                blocker = blockers[0]
            print('')
            print(blocker.name,'decides to block',current.name)
            return blocker
        else:
            return False

    def loose_card(looser):
        print(looser.name,'wich card are you going to loose:',looser.cards_self)
        card = input()
        if card not in looser.cards_self:
            print('Invalid choice')
            return Logic.loose_card(looser)
        looser.cards_self.remove(card)
        looser.cards_shown.remove('*')
        looser.cards_shown.append(card)
        print()
        print(looser.name,'looses his',card)                

    def change_card(current,card):
        current.cards_self.remove(card)
        current.cards_shown.remove(card)
        deck.append(card)
        shuffle(deck)
        new = deck[0]
        current.cards_self.append(new)
        current.cards_shown.append('*')
        print()
        print(current.name,'your new cards:',current.cards_self)

    def exchange_method(number,current,deck):
        if number == 1:
            card = current.cards_self[0]
            new = [deck[0],deck[1],card]
            print()
            print(current.name,'your card:',current.cards_self)
            current.cards_self.remove(card)
            deck.pop(0)
            deck.pop(1)
            print(current.name,'wich one of these cards do you pick')
            print(new)
            choice = input()
            while choice not in new:
                print('Invalid choice, try again')
                choice = input()
            new.remove(choice)
            current.cards_self.append(choice)
            for back in new:
                deck.append(back)
            shuffle(deck)
            print()
            print(current.name,'exchanged his/her card!')
        else:
            print()
            print(current.name,'your cards:',current.cards_self)
            new = [deck[0],deck[1],current.cards_self[0],current.cards_self[1]]
            deck.pop(0)
            deck.pop(1)
            current.cards_self.pop(0)
            current.cards_self.pop(0)    
            print(current.name,'pick your first card')
            print(new)
            choice1 = input()       
            while choice1 not in new:
                print('Invalid choice, try again')
                choice1 = input()
            new.remove(choice1)
            current.cards_self.append(choice1)
            print()
            print(current.name,'pick your second card')
            print(new)
            choice2 = input()       
            while choice2 not in new:
                print('Invalid choice, try again')
                choice2 = input()
            new.remove(choice2) 
            current.cards_self.append(choice2)
            for back in new:
                deck.append(back)
            shuffle(deck)
            print()
            print(current.name,'exchanged his/her cards!')

    def foreign_aid(current,active_players):
        card = 'Duke'
        counter = Logic.counter(active_players,current)
        if not counter:
            print('')
            print(current.name,'takes 2 coins!')
            return True
        blocker = counter
        challenge = Logic.challenge(blocker,active_players,card)
        if challenge:
            print('\nThe counter won the challenge,',current.name,'cannot take 2 coins')
            return False
        if challenge == 'no one':
            print(current.name,'cannot take 2 coins')
            return False
        else:
            print('\nThe counter lost the challenge,',current.name,'takes 2 coins!')
            return True

    def coup(current,active_players):
        print(current.name,'which player do you coup:')
        attacked = input('')
        flag = False
        for a in active_players:
            if attacked == a.name and attacked != current.name:
                attacked = a
                flag = True
                break
        if not flag:
            print('Invalid player, try again')
            return Logic.coup(current, active_players)
        print('')
        print(current.name,'coups',attacked.name+'!')
        Logic.loose_card(attacked)

    def tax(current,active_players):
        card = 'Duke'
        challenge = Logic.challenge(current,active_players,card)
        if challenge:
            print()
            print(current.name,'takes 3 coins!')
            return True
        else:
            print()
            print(current.name,'cannot take 3 coins')
            return False

    def assasinate(current,active_players):
        card = 'Assasin'
        print(current.name,'which player do you assasinate:')
        attacked = input('')
        flag = False
        for a in active_players:
            if attacked == a.name and attacked != current.name:
                attacked = a
                flag = True
                break
        if not flag:
            print('\nInvalid player, try again')
            return Logic.assasinate(current, active_players)
        print('')
        print(current.name,'decides to assasinate',attacked.name+'!')
        challenge = Logic.challenge(current,active_players,card)
        if challenge:
            if len(attacked.cards_self) == 0:
                print(attacked.name,'has no more cards')
                return 0
            blocker = Logic.counter(active_players, current)
            if not blocker:
                print()
                print(current.name,'assasinates',attacked.name)
                Logic.loose_card(attacked)
                return True
            card = 'Contessa'
            challenge = Logic.challenge(blocker,active_players,card)
            if challenge:
                if len(attacked.cards_self) == 0:
                    print(attacked.name,'has no more cards')
                    return 0
                print(blocker.name,'blocks',current.name,'assasination!')
                return True
            if challenge == 'no one':
                print(blocker.name,'blocks',current.name,'assasination!')
                return True
            if not challenge:
                print(current.name,'assasinates',attacked.name)
                Logic.loose_card(attacked)
                return True
        else:
            print()
            print(current.name,'cannot assasin',attacked.name)

    def exchange(current,active_players):
        number = len(current.cards_self)
        card = 'Ambassador'
        challenge = Logic.challenge(current,active_players,card)
        if challenge or  challenge == 'no one':
            Logic.exchange_method(number, current, deck)
            return True
        else:
            print('')
            print(current.name,'lost the challenge, so he/she cannot exchange his/her cards\n')
            return False
        print('')

    def steal(current,active_players):
        card = 'Captain'  
        print(current.name,'which player would you like to steal from ? :')
        stoled = input('')
        flag = False
        for a in active_players:
            if stoled == a.name and stoled != current.name:
                stoled = a
                flag = True
                break
        if not flag:
            print('\nInvalid player, try again')
            return Logic.steal(current, active_players)
        print('')
        print(current.name,'decides to steal from',stoled.name+'!')
        challenge = Logic.challenge(current,active_players,card)
        if challenge:
            blocker = Logic.counter(active_players, current)
            if not blocker:
                print()
                print(current.name,'stole from',stoled.name)
                stoled.coins -= 2
                return True
            challenge = Logic.challenge(blocker,active_players,card)
            if challenge:
                print(blocker.name,'blocks',current.name,'steal!')
                return False
            if challenge == 'no one':
                print(blocker.name,'blocks',current.name,'steal!')
                return False
            if not challenge:
                print(current.name,'stole from',attacked.name)
                Logic.loose_card(attacked)
                stoled.coins -= 2
                return True
        else:
            print()
            print(current.name,'cannot steal from',stoled.name)
        print('')