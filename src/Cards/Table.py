''' Created on Oct 25, 2017
    @author: Wonsil and Shannon '''

from Deck import Deck

class Table(object):

    def __init__(self, numPlayers):
        self.players = []
        self.numPlayers = numPlayers
        self.deck = Deck()
    
    def getNumOfPlayers(self):
        return self.numPlayers   
        
    def getHands(self):
        return self.players 
    
    def deal(self, numOfCards):
        
        if numOfCards * len(self.players) > self.deck.Size():
            raise ValueError
        else:
            for _ in range(self.numPlayers):
                self.players.append(self.deck.DealOut(numOfCards))
                