'''
Created on Oct 25, 2017

@author: Wonsil and Shannon
'''
import unittest
from Deck import *
from Card import *

class DeckTest(unittest.TestCase):

    def testConstruction(self):
        suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
        testDeck0 = Deck()
        
        for x in range(2,15):
            for y in suits:
                self.assertEquals(testDeck0.IsCard(x,y), True, "Card: " + str(x) + " of " + y + " was not constructed correctly")
                
    def testShuffle(self):
        testDeck1 = Deck()
        unshuffled = testDeck1.GetDeck()
        
        testDeck1.Shuffle()
        
        self.assertNotEquals(testDeck1.GetDeck(), unshuffled, "The deck has not been shuffled.")
        
    def testNumCardsDealt(self):
        testDeck2 = Deck()
        
        cards0 = testDeck2.DealOut(10)
        
        self.assertEquals(len(cards0), 10, "The number of cards dealt out was not correct.")
        self.assertEqual(testDeck2.Size(), 42, "The number of cards removed from deck was not correct")
        
    def testNumCardsDealtExceedsDeck(self):
        testDeck3 = Deck()
      
        try:
            cards1 = testDeck3.DealOut(54)
            self.assertsFalse(len(cards1), 54, "This number exceeds the number of cards in the deck." )
        except ValueError:
            pass
        
    def testMultipleCardsThatExceedDeck(self):
        testDeck4 = Deck()
        
        cards2 = testDeck4.DealOut(20)
        
        self.assertEqual(len(cards2), 20, "The number of cards was not dealt correctly")
        self.assertEqual(testDeck4.Size(), 32, "The number of cards removed from deck was not correct")
        try:
            cards3 = testDeck4.DealOut(40)
            self.assertFalse(len(cards3), 40, "Dealt too many cards")
        except ValueError:
            pass
        
    def testDeckRemoval(self):
        testDeck5 = Deck()
        
        card0 = testDeck5.DealOut(1)
        
        self.assertEqual(testDeck5.IsCard(card0[0].GetValue(), card0[0].GetSuit()), False, "Card was not removed from deck")
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()