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
        
class Cashpyment(PaymentMethod):
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
    
# user interface 

class PizzaShop(PizzaShopInterface):
    def __init__(self):
        self.orders = []
    
    def choose_pizza(self) -> Pizza:
        print("Our pizzas:")
        print("1. Margherita: 10$")
        print("2. Pepperoni: 15$")
        print("3. Hawaiian: 13$")
        print("4. Meat: 17$")
        print("5. Ham and mushrooms: 15$")
        
        choice = int(input("Choose your pizza: "))
        if choice == 1:
            return Pizza("Margherita", 10.0)
        if choice == 2:
            return Pizza("Pepperoni", 15.0)
        if choice == 3:
            return Pizza("hawaiian", 13.0)
        if choice == 4:
            return Pizza("Meat", 17.0)
        if choice == 5:
            return Pizza("Ham and mushrooms", 10.0)
        else:
            print("Incorrect input. Setting Margherita by default")
            return Pizza("Margherita", 10.0)
        
    def create_custom_pizza(self) -> Pizza:
        name = input("Enter the name for your pizza: ")
        base_price = 12
        print("You can choose any 4 toppins for a base price of 12$")
        custom_pizza = Pizza(name, base_price)
        
        # counter for limit of topping number 
        topping_counter = 0
        max_toppings = 4
        while topping_counter < max_toppings:
            topping = input(f"Enter topping:
                            1. sweet onion
                            2. jalapeno
                            3. chili
                            4. pickle
                            5. olives
                            6. prosciutto
                            or 'done' to finish): ")
            if topping.lower() == 'done':
                break
            price = 0 # toppings do not increase the price 
        custom_pizza.add_topping(topping, price)
        topping_counter += 1
        if topping_counter == max_toppings:
            print("Maximum amounts of toppings has been reached")
            return custom_pizza
    
# admin interface   

class Admin(AdminShopInterface):
    def __init__(self, orders: List[Order]):
        self.orders = orders
        
    def get_sales_report(self):
        total_pizzas = len(self.orders)
        total_revenue = sum(order.pizza.calculate_price() for order in self.orders)
        profit_margin = 0.3 # 30% from revenue is profit
        total_profit = total_revenue * profit_margin
        
        print(f"Total pizzas sold: {total_pizzas}")
        print(f"Total revenue: {total_revenue} $")
        print(f"Total profit: {total_profit} $")
        
# main programm 
if __name__ == "__main__":
    shop = PizzaShop()
    while True:
        print("\n Welcome to the Pizzeria 'Roi'! ")
        print("1. Choose a pizza")
        print("2. Create a custom pizza")
        print("3. Exit")
        choice = int(input("Choose from options above: "))
        if choice == 1:
            pizza = shop.choose_pizza()
        elif choice == 2:
            pizza = shop.create_custom_pizza()
        elif choice == 3:
            break
        else:
            print("Invalid choice, try again")
            continue
        
        print("\n Choose payment method")
        print("1. Card")
        print("2. Cash")
        payment_choice = int(input("Choose 1/2: "))
        if payment_choice == 1:
            payment_method = CardPayment()
        elif payment_choice == 2:
            payment_method = Cashpyment()
        else: 
            print("Invalid choice, try again")
            continue
        
# admin mode 
admin = Admin(shop.orders)
admin.get_sales_report
        
        
        