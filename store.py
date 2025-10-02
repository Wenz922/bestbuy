from typing import List
from products import Product


class Store:

    def __init__(self, product_list):
        if product_list:
            self.product_list = product_list
        else:
            self.product_list = []

    def add_product(self, product):
        """Add a new product to the store"""
        self.product_list.append(product)

    def remove_product(self, product):
        """Remove a product from the store"""
        if product in self.product_list:
            self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Return total quantity of products in the store"""
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self) -> List[Product]:
        """Return all active products in the store"""
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """Buy products with quantity and return the total price of the order.
        If any product fails, the order is cancelled.
        shopping_list is a list of tuples (product, quantity)"""
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(f"Order failed for {product.name}: {e}")
                return 0  # cancel the order, return 0
        return total_price
