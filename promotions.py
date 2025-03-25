from abc import ABC, abstractmethod



class Promotion(ABC):
    def __init__(self, description, percent =0):
        self.description = description
        self._discount = percent

    @abstractmethod
    def apply_promotion(self, product, quantity):
        discounted_price = product.price * (1-self._discount)
        return discounted_price * quantity

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        total_price = 0
        for i in range(quantity):
            if i % 2 == 1:
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
        discounted_price = product.price * (1-self._discount)
        return discounted_price * quantity

second_half_price = SecondHalfPrice("Second Half price!")
# print(promotions.self.description)