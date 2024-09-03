from abc import ABC, abstractmethod
from typing import List

class Pizza:
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping: str, price: float):
        self.toppings.append((topping, price))

    def calculate_price(self) -> float:
        return self.base_price + sum(price for _, price in self.toppings)

class Order:
    def __init__(self, pizza: Pizza, payment_method):
        self.pizza = pizza
        self.payment_method = payment_method

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} $ with credit card.")

class CashPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} $ in cash.")

class PizzaShop(ABC):
    def __init__(self):
        self.orders = []

    def choose_pizza(self) -> Pizza:
        
        print("Available pizzas:")
        print("1. Margherita - $10")
        print("2. Pepperoni - $12")
        print("3. Hawaiian - $11")

        choice = int(input("Choose a pizza by number: "))
        if choice == 1:
            return Pizza("Margherita", 10)
        elif choice == 2:
            return Pizza("Pepperoni", 12)
        elif choice == 3:
            return Pizza("Hawaiian", 11)
        else:
            print("Invalid choice, defaulting to Margherita.")
            return Pizza("Margherita", 10)

    def create_custom_pizza(self) -> Pizza:
        name = input("Enter the name for your pizza: ")
        base_price = 12
        print("You can choose any 4 toppings for a base price of 12$")
        custom_pizza = Pizza(name, base_price)

        topping_count = 0
        max_toppings = 4

        while topping_count < max_toppings:
            print("Choose between these toppings (enter number) OR type 'done' to finish:")
            print("1. Sweet onion")
            print("2. Jalapeno")
            print("3. Chili")
            print("4. Pickle")
            print("5. Olives")
            print("6. Prosciutto")
            topping = input(f"Choice {topping_count + 1}:  ")
            if topping.lower() == 'done':
                break
            price = 0
            

        return custom_pizza

    @abstractmethod
    def place_order(self, pizza: Pizza, payment_method: PaymentMethod):
        pass

class MyPizzaShop(PizzaShop):
    def place_order(self, pizza: Pizza, payment_method: PaymentMethod):
        order = Order(pizza, payment_method)
        self.orders.append(order)
        amount = pizza.calculate_price()
        payment_method.pay(amount)
        print(f"Order placed for {pizza.name}. Total amount: {amount} $")

class Admin:
    def __init__(self, orders: List[Order]):
        self.orders = orders
        
    def get_sales_report(self):
        total_pizzas = len(self.orders)
        total_revenue = sum(order.pizza.calculate_price() for order in self.orders)
        profit_margin = 0.3  # 30% от выручки - это прибыль
        total_profit = total_revenue * profit_margin
        
        print(f"Total pizzas sold: {total_pizzas}")
        print(f"Total revenue: {total_revenue} $")
        print(f"Total profit: {total_profit} $")


# Основная программа
if __name__ == "__main__":
    shop = MyPizzaShop()
    while True:
        print("\nWelcome to the Pizzeria 'Roi'!")
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

        print("\nChoose payment method:")
        print("1. Card")
        print("2. Cash")

        payment_choice = int(input("Choose 1/2: "))

        if payment_choice == 1:
            payment_method = CreditCardPayment()
        elif payment_choice == 2:
            payment_method = CashPayment()
        else:
            print("Invalid choice, try again")
            continue

        shop.place_order(pizza, payment_method)

    admin = Admin(shop.orders)
    admin.get_sales_report()