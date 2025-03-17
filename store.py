from typing import get_args

import products
from products import Product


class Store:
    def __init__(self, products=None):
        if products is None:
            products =[]
        if not isinstance(products, list):
            raise TypeError("product must be a list")
        self.products = products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only instances of class Product accepted.")
        self.products.append(product)

    def remove_product(self, product):
        pass

    def get_total_quantity(self):
        total_quan = []
        for product in self.products:
            total_quan.append(product.quantity)
        return sum(total_quan)

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product.quantity < quantity:
                raise ValueError("Not enough in stock")
            product.quantity -= quantity
            total_price += product.price * quantity
        return f'Order costs: {total_price} dollars.'

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]
best_buy = Store(product_list)
a_products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(a_products[0], 1), (a_products[1], 2)]))