from itertools import product
from logging import raiseExceptions


class Product:
    """creating a class with the attributes of product name price and quantity, that
    updates everytime the buy function or set_quantity is executed ."""
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or name == "":
            raise TypeError("please enter a name for the product")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("the price has to be 0 or higher")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("the quantity has to be 0 or higher")
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self._active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity


    def is_active(self):
        return self.quantity > 0


    def activate(self):
        self._active = True
        print(f"{self.name} is already active")


    def deactivate(self):
        if self._active:
            self._active = False
            print(f'{self.name} has been deactivated')
        else:
            print(f'{self.name} is already deactivated')


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError

        self.quantity -= quantity
        show_price = self.price * quantity
        return f'The total price for your {quantity} {self.name} is {show_price}'


class NonStockedProduct(Product):
    def __init__(self, name, price,quantity):
        super().__init__(name, price, quantity)
        self.quantity = 0

    def is_active(self):
        return True

    def buy(self, quantity):
        show_price = self.price * quantity
        return f'The total price for your {quantity} {self.name} is {show_price}'

    def show(self):
        print(f"{self.name}, Price: {self.price}")

class LimitedProduct(Product):
    def __init__(self, name, price,quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError

    def show(self):
        print(f"{self.name}, Price: {self.price}")