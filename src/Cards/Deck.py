'''
Created on Oct 25, 2017

@author: Wonsil and Shannon
'''
from Card import *
from random import shuffle

class Deck(object):



    def __init__(self):
        self.cards = [Card(x, y) for x in range(2, 15) for y in ["Hearts", "Diamonds", "Clubs", "Spades"]]
        self.size = len(self.cards)
        
    def IsCard(self, value, suit):
        retVal = False
        for card in self.cards:
            if card.GetCard() == Card(value,suit).GetCard():
                retVal = True
                break
        
        return retVal
    
    def GetDeck(self):
        return self.cards
    
    def Shuffle(self):
        self.cards = shuffle(self.cards)
    