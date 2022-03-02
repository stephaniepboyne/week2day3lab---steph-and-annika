import unittest

from src.pub import Pub
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("whisky", 4.00)
    
    def test_drink_has_name(self): 
        self.assertEqual("whisky", self.drink.name)
    
    def test_drink_price(self):
        expected = 4.00
        actual = self.drink.price
        self.assertEqual(expected, actual)


