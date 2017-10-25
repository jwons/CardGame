'''
Created on Oct 24, 2017

@author: Wonsil and Shannon
'''
import unittest
from Card import *


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testValidCardNumber(self):
        testCard0 = Card(3,"Spades")
        self.assertEqual(testCard0.GetSuit(), "Spades", "Failed constructing correct suit 3 of spades")
        self.assertEqual(testCard0.GetValue(), 3, "Failed constructing correct suit 3 of spades")
        
    def testValidJackFace(self):
        testCard1 = Card(11,"Spades") #Jack
        self.assertEqual(testCard1.GetSuit(), "Spades", "Failed constructing correct suit Jack of spades")
        self.assertEqual(testCard1.GetValue(), 11, "Failed constructing correct suit Jack of spades")
        
    def testValidQueenFace(self):
        testCard2 = Card(12,"Hearts") #Queen 
        self.assertEqual(testCard2.GetSuit(), "Hearts", "Failed constructing correct suit Queen of Hearts")
        self.assertEqual(testCard2.GetValue(), 12, "Failed constructing correct suit Queen of Hearts")
        
    def testValidKingFace(self):
        testCard3 = Card(13,"Diamonds") #King
        self.assertEqual(testCard3.GetSuit(), "Diamonds", "Failed constructing correct suit King of Diamonds")
        self.assertEqual(testCard3.GetValue(), 13, "Failed constructing correct suit King of Diamonds")
        
    def testValidAce(self):
        testCard4 = Card(14, "Clubs") #Ace or 14
        self.assertEqual(testCard4.GetSuit(), "Clubs", "Failed constructing correct suit Ace of Clubs")
        self.assertEqual(testCard4.GetValue(), 14, "Failed constructing correct suit Ace of Clubs") 
        
    def testInvalidLowNum(self):
        try:
            testCard5 = Card(-1, "Clubs")
            self.assertFalse(testCard5.GetValue(), -1, "Shouldn't be able to construct a 16 of Clubs")
        except ValueError:
            pass
    
    def testInvalidHighNum(self):
        try:
            testCard6 = Card(16, "Clubs")
            self.assertFalse(testCard6.GetValue(), 16, "Shouldn't be able to construct a 16 of Clubs")
        except ValueError:
            pass
        
    def testGetCard(self):
        testCard7 = Card(14,"Spades")
        self.assertEqual(testCard7.GetCard(), "A of Spades", "Failed to correctly return the Ace of Spades")
        
    def testGetCardNum(self):
        testCard8 = Card(3,"Spades")
        self.assertEqual(testCard8.GetCard(), "3 of Spades", "Failed to correctly return the 3 of Spades")
   


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()