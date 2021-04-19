from numpy import random
from random import shuffle
from deck import Deck
from player import Player

class Logic:

    @classmethod
    def __challenge(cls,challenged,players,card):
        challengers = []
        for challenge in players:
            if challenged.name == challenge.name:
                continue
            print(challenge.name,'Do you want to challenge',challenged.name,'counter?(y/n):')
            if r == 'y':
                challengers.append = challenge
            
            if len(challengers) > 0:
                challenger = challengers[random.randint(0,len(challengers)-1)]
                print('')
                print(challenger.name,'decides to challenge',challenged.name,'Counter!')
                print(challenged.name,'cards:')
                if card in challenged.cards:
                    print('['+str(card),'*]')
                    print(challenged.name,'has a',card+'!\n')
                    print(challenger.name,'you lost the challenge, wich one of your cards do you loose')
                    return False
                else:
                    print('You dont have the',card,'wich one of your cards do you loose(0/1)')
                    return True
            else: 
                return False
                

    #public_method
    def foreign_aid(current,players):
        blockers = []
        card = 'Duke'
        for block in players:
            if current.name == block.name:
                continue
            print(block.name,'You have a Duke, Do you want to block',current.name,'Foreign Aid(y/n)?:')
            if r == 'y':
                blockers.append = block

        if len(blockers) > 0:
            blocker = blockers[random.randint(0,len(blockers)-1)]
            print('')
            print(blocker.name,'decides to block',current.name,'Foreign Aid!')
            if cls.__challenge(blocker,players,card):
                print('bap')
       
        else:
            return False
