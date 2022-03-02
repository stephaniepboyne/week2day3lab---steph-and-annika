from src.customer import Customer
from src.drink import Drink

class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks 
    
    def increase_till(self, amount):
        self.till += amount

    def decrease_till(self, amount):
        self.till -= amount 
    
    def check_customer_age(self, anme):
        if self.customer.age >= 18:
            return "Hurray! Customer is 18 or over."
    
    def customer_buys_drink(self):
        self.customer.wallet -= self.drink.price 
        self.till += self.drink.price

    






    
    

    

