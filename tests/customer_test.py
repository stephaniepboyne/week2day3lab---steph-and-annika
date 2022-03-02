import unittest

from src.pub import Pub
from src.customer import Customer 
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("George", 10.00, 19)


    def test_customer_has_name(self):
        self.assertEqual("George", self.customer.name)
    
    def test_customer_cash(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_customer_can_buy_drink(self):
        drink = Drink("whisky", 4.00)
        self.customer.buy_drink(drink)
        self.assertEqual(6.00, self.customer.wallet)

    
    
