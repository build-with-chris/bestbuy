from products import Product, NonStockedProduct, LimitedProduct


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
            if not isinstance(product, NonStockedProduct):
                if product.quantity < quantity:
                    raise ValueError("Not enough in stock")

            total_price += product.buy(quantity)
        return f'Order costs: {total_price} dollars.'

