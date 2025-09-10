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
        total_product = 0
        for product in self.product_list:
            total_product += product.get_quantity()
        return total_product

    def get_all_products(self) -> List[Product]:
        """Return all active products in the store"""
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """Buy products with quantity and return the total price of the order
        shopping_list is a list of tuples (product, quantity)"""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
