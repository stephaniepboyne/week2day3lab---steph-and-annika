from src.customer import Customer
from src.drink import Drink


class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = []
    
    def increase_till(self, amount):
        self.till += amount

    def decrease_till(self, amount):
        self.till -= amount 
    
    def check_customer_age(self, customer):
        return customer.age >= 18
    
    # def customer_buys_drink(self, customer):
    #     customer.wallet -= self.drink.price 
    #     self.till += self.drink.price

    






    
    

    

