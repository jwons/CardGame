'''
Created on Oct 26, 2017

@author: Wonsil and Shannon
'''
import unittest
from CardUnitTest import CardTest
from DeckUnitTests import DeckTest
from TableUnitTests import TableTest

if __name__ == "__main__":
    unitTests = [CardTest, DeckTest, TableTest]
    
    loader = unittest.TestLoader()
    
    suites_list =[]
    for unitTest in unitTests:
        suite = loader.loadTestsFromTestCase(unitTest)
        suites_list.append(suite)
        
    bigSuite = unittest.TestSuite(suites_list)
    
    runner = unittest.TextTestRunner()
    results = runner.run(bigSuite)
    
    