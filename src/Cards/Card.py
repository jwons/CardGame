''' Created on Oct 24, 2017
    @author: Wonsil and Shannon '''

class Card():
    
    def __init__(self, value, suit):
        self._checkParams(value, suit)
        
    def _checkParams(self, value, suit):
        
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        valDict = {11:"J", 12:"Q", 13:"K", 14:"A"}
        
        
        # Check to see if value is within range
        if type(value) == int:
            
            if value in range(1, 15):
                self.value = value
                
                # Check to see if value has face value
                if value in valDict:
                    self.stringValue = valDict[value]
                else:
                    self.stringValue = str(value)
                    
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
    
    def GetCard(self):
        return self.stringValue + " of " + self.suit