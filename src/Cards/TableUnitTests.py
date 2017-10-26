'''
Created on Oct 25, 2017

@author: Wonsil
'''
import unittest
from Table import *

class TableUnitTest(unittest.TestCase):

    def testNumPlayers(self):
        table0 = Table(2)
        
        self.assertEqual(table0.getNumOfPlayers(), 2, "Number of players not initialized.")
        
    def testHandSize(self):
        table1 = Table(4)
        table1.deal(5)
        playersCards1 = table1.getHands()
        
        for hand in playersCards1:
            self.assertEqual(len(hand), 5, "Hand size was incorrectly dealt")
            
    def testHandSizeExceeding(self):
        table2 = Table(4)
        
        try:
            table2.deal(15)
            playersCards2 = table2.getHands()
            
            for hand in playersCards2:
                self.assertEqual(len(hand), 15, "Hand size exceeded total number of cards")
            
        except ValueError:
            pass
        
    def testNegativePlayers(self):
        try:
            table3 = Table(-3)
            playersCards3 = table3.getHands()
            self.assertEqual(len(playersCards3), 0, "Number of players initialized incorrect")
        except ValueError:
            pass
        
    def testNegativeCards(self):
        table4 = Table(2)
        
        try:
            table4.deal(-3)
            playersCards4 = table4.getHands()
            for hand in playersCards4:
                self.assertEqual(len(hand), 0, "Hand size attempted to be negative")
        except ValueError:
            pass
        
if __name__ == "__main__":
    unittest.main()