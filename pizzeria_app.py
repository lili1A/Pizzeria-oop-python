from abc import ABC, abstractmethod
from typing import List 

# SRP: class Pizza is responsible for data aand operations connected with pizza

class Pizza:
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.topping = []
        
    def add_topping(self, topping: str, price: float):
        self.topping.append((topping, price))
        
    def calculate_price(self) -> float:
        return self.base_price + sum(price for _, price in self.topping)
    
    def __str__(self):
        toppings_str = ",".join([t[0] for t in self.topping]) or "No toppings"
        return f"{self.name} (Base price: {self.base_price}$, Toppings: {toppings_str})- Total: {self.calculate_price}$"
    
# OCP: payment classes expand withoud changing the code 

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} $ amount with card")
        
class Cashayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} $ amount with cash")
        
# LSP: class order doesn't interfere in the working process of other classes

class Order:
    def __init__(self, pizza: Pizza, payment_method: PaymentMethod):
        self.pizza = pizza
        self.payment_method = payment_method
        
    def process_order(self):
        amount = self.pizza.calculate_price()
        self.payment_method.pay(amount)
        self.save_order_to_file()

    def save_order_to_file(self):
        with open("order.txt", "a") as file:
            file.write(str(self.pizza) + "\n")
        print(f"Order saved: {self.pizza}")
        
# ICP: user and admin interface 

class PizzaShopInterface(ABC):
    @abstractmethod
    def choose_pizza(self):
        pass
    @abstractmethod
    def create_custom_pizza(self):
        pass
    @abstractmethod
    def place_order(self, pizza: Pizza, payment_method: PaymentMethod):
        pass
    
class AdminShopInterface(ABC):
    @abstractmethod
    def get_sales_report(self):
        pass