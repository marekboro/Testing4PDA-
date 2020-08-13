import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.suit = "Diamonds"
        card_value1 = 2
        card_value2 = 1
        self.card1 = Card(self.suit,card_value1)
        self.ace_of_diamonds = Card(self.suit,card_value2)
        self.cards = [self.card1,self.ace_of_diamonds]

    def test_card_value(self):
        actual = self.card1.value
        expected = 1                                # to fail test
        expected = 2                                # comment out current line to have the previous one fail test.
        self.assertEqual(expected,actual)

    def test_check_for_ace_method(self):
        actual = CardGame.checkforAce(self,self.ace_of_diamonds)
        expected = False                            # to fail test
        expected = True                             # comment out current line to have the previous one fail test.
        self.assertEqual(expected,actual)
    
    def test_highest_card(self):
        actual = CardGame.highest_card(self,self.ace_of_diamonds,self.card1)
        expected = Card(self.suit,1)               # to fail test
        expected = self.card1                       # comment out current line to have the previous one fail test.
        self.assertEqual(expected,actual)

    def test_cards_total(self):
        actual = CardGame.cards_total(self,self.cards)
        expected = "You have a total of 1"          # to fail test
        expected = "You have a total of 3"          # comment out current line to have the previous one fail test.
        self.assertEqual(expected,actual)
    