import unittest
import random
from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        suit1 = "Hearts"
        suit2 = "Diamonds"
        suit3 = "Clubs"
        suit4 = "Spades"
        
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        card_value1 = 2
        card_value2 = 1
        card_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

        self.card1 = Card(suit1,card_value1)
        self.randomCard= Card(random.choice(suits),random.choice(card_values))
        self.ace_of_diamonds = Card(suit2,card_value2)

    def test_card_value(self):
        actual = self.card1.value
        expected = 1
        expected = 2
        self.assertEqual(expected,actual)

    def test_check_for_ace_method(self):
        actual = CardGame.checkforAce(self,self.ace_of_diamonds)
        expected = False
        #expected = True
        self.assertEqual(expected,actual)

    