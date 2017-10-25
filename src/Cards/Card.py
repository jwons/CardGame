'''
Created on Oct 24, 2017

@author: Wonsil and Shannon
'''

class Card():
    
    def __init__(self, value, suit):
        self._checkParams(value, suit)
        
    def _checkParams(self, value, suit):
        
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        
        # Check to see if value is within range
        if type(value) == int:
            if value > 0 and value < 15:
                self.value = value
            else:
                raise ValueError
              
        # Check to see if suit is valid   
        if type(suit) == str:
            if suit in suits:
                self.suit = suit
            else:
                raise TypeError
                
    def GetValue(self):
        return self.value
    
    def GetSuit(self):
        return self.suit

        