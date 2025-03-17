from itertools import product
from logging import raiseExceptions


class Product:
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
        if self.quantity == 0 and self._active:
            self.deactivate()
            return False


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


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)

mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(250))
print(mac.buy(100))
print(mac.is_active())
mac.show()
bose.show()
bose.set_quantity(1000)
bose.show()

bose.show()


