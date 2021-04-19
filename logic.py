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
            print('Do you want to challenge',challenged.name,'counter?(y/n):')
            r = input()
            if r == 'y':
                challengers.append(challenge)
        
        if len(challengers) > 0:
            if len(challengers) > 1:
                challenger = challengers[random.randint(0,len(challengers)-1)]
            if len(challengers) == 1:
                challenger = challengers[0]
            print('')
            print(challenger.name,'decides to challenge',challenged.name,'Counter!\n')                
            print(challenged.name,'cards:')
            if card in challenged.cards:
                    print('['+str(card),', * ]')
                    print(challenged.name,'has a',card+'!\n')
                    print(challenger.name,'you lost the challenge, wich one of your cards do you loose')
                    return True
            else:
                print('You dont have the',card,'wich one of your cards do you loose(0/1)')
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
            print('Do you want to block',current.name,'Foreign Aid(y/n)?:')
            r = input()
            if r == 'y':
                blockers.append(block)

        if len(blockers) > 0:
            if len(blockers) > 1:
                blocker = blockers[random.randint(0,len(blockers)-1)]
            if len(blockers) == 1:
                blocker = blockers[0]
            print(blocker.name,'decides to block',current.name,'Foreign Aid!')
            return blocker
        else:
            return False

                

    #public_methods
    def foreign_aid(current,players):
        card = 'Duke'
        counter = Logic.counter(players,current)
        if not counter:
            print('')
            print(current.name,'takes 2 coins!')
            return True

        blocker = counter
        challenge = Logic.challenge(blocker,players,card)
        if challenge:
            print('\nThe counter won the challenge,',current.name,'cannot take 2 coins')
            return False
        if challenge == 'no one':
            print(current.name,'cannot take 2 coins')
            return False
        else:
            print('The counter lost the challenge,',current.name,'takes 2 coins!')
            return True


    def coup(current,players):
        print(current.name,'which player do you coup:')
        attacked = input('')
        flag = False
        for a in players:
            if attacked == a.name and attacked != current.name:
                flag = True
                break
        if not flag:
            print('Invalid player, try again')
            return Logic.coup(current, players)
        print('')
        print(current.name,'coups',attacked+'!')

        

