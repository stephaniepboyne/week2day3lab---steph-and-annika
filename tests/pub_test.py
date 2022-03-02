import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, [])
        self.customer_1 = Customer("George", 10.00, 19)
        self.customer_2 = Customer("Beth", 5.00, 16)
        self.drink_1 = Drink("Whisky", 12.00)
        self.drink_2 = Drink("Beer", 6)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)
    
    def test_decrease_till(self):
        self.pub.decrease_till(4.00)
        expected = 96.00
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_customer_age(self): 
        self.assertEqual(True, self.pub.check_customer_age(self.customer_1)) 
        self.assertEqual(False, self.pub.check_customer_age(self.customer_2)) 

   
    
        

    

        





    

