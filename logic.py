from numpy import random
from random import shuffle
from deck import Deck
from player import Player

class Logic:

    #public_methods
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
            if card in challenged.cards_self:
                    challenged.cards_shown.remove('*')
                    challenged.cards_shown.append(card)
                    print(challenger.name,'cards:',challenged.cards_shown)
                    print(challenged.name,'has a',card+'!\n')
                    print(challenged.name,'you lost the challenge')
                    Logic.loose_card(challenger)
                    return True
            else:
                print(challenged.name,'You dont have the',card)
                Logic.loose_card(challenged)
                return False
        else: 
            print('Nobody challenged',challenged.name)
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
        print(looser.name,'wich one of your cards do you loose:',looser.cards_self)
        card = input()
        if card not in looser.cards_self:
            print('Invalid choice')
            return Logic.loose_card(looser,players)
        
        looser.cards_self.remove(card)
        looser.cards_shown.remove('*')
        looser.cards_shown.append(card)
        print(looser.name,'looses his',card)                

    #public_methods
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
        else:
            print()
            print(current.name,'cannot take 3 coins')
        



        

