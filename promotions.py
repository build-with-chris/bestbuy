from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, description, percent =0):
        self.description = description
        self._discount = percent

    @abstractmethod
    def apply_promotion(self, product, quantity=1):
        '''zwingend nötig für eine Promotion'''
        pass

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        total_price = 0
        for i in range(1, quantity+1):
            if i % 2 == 0:
                total_price += 0.5 * product.price
            else:
                total_price += product.price
        return total_price

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        total_price = 0
        for i in range(quantity):
            if (i+1) % 3 == 0:
                continue
            total_price += product.price
        return total_price

class PercentDiscount(Promotion):
    def __init__(self, description, discount):
        super().__init__(description, discount)

    def apply_promotion(self, product, quantity):
        total_price = product.price * (1-self._discount/100) * quantity
        return total_price

