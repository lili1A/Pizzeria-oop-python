from new_app_pizzeria import List
from new_app_pizzeria import Order 

class Admin:
    def __init__(self, orders: List[Order]):
        self.orders = orders
        
    def get_sales_report(self):
        total_pizzas = len(self.orders)
        total_rev = sum(order.pizza.calculate_price() for order in self.orders)
        profit_margin = 0.3
        total_profit = total_rev * profit_margin
        
        print(f"Total pizza sold: {total_pizzas}")
        print(f"Total revenue: {total_rev} $")
        print(f"Total profit: {total_profit} $")
        
