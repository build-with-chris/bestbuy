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

    def set_promotion(self, promotion):
        self.promotion = promotion



    def buy(self, quantity):
        """Check if the quantity in stock is sufficient and applies promotion if available.
        returns the total price for one product"""
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        self.quantity -= quantity
        if hasattr(self, "promotion") and self.promotion:
            print(f"Applying promotion to {self.name}: {self.promotion.description}")
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        return total_price


class NonStockedProduct(Product):
    '''a class that handles products that don't depend on quantity
    we do not adjust quantity of the product in this class for the buy methode'''
    def __init__(self, name, price,quantity= 0):
        super().__init__(name, price, quantity)

    def is_active(self):
        return True

    def buy(self, quantity):
        if hasattr(self, "promotion") and self.promotion:
            print(f"Applying promotion to {self.name}: {self.promotion.description}")
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        return total_price

    def show(self):
        print(f"{self.name}, Price: {self.price:.0f}")

class LimitedProduct(Product):
    '''A class that handles a product with maximum amount per order
    we raise an error if the maximum is exceeded.'''
    def __init__(self, name, price,quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Only one shipping allowed")
        else:
            total_price = self.price * quantity
        return total_price

    def show(self):
        print(f"{self.name}, Price: {self.price}")



