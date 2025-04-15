from products import Product, NonStockedProduct, LimitedProduct

class Store:
    """A class to describe a shopping list of non, single or multiple items and quantity"""
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
        self.products.remove(product)

    def get_total_quantity(self):
        """This function returns the total quantity over all products"""
        total_quan = []
        for product in self.products:
            total_quan.append(product.quantity)
        return sum(total_quan)


    def get_all_products(self):
        """This function returns all the active products in the shop setup"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def validate_order(self, shopping_list):
        """check if there is one or multiple errors in the input to stop executing the order
        function already before it is executed for the first item."""
        for product, quantity in shopping_list.items():
            if isinstance(product, LimitedProduct):
                if product.quantity > product.maximum:
                    raise ValueError(f"Error. Only {product.maximum} shipping allowed.")
            if not isinstance(product, NonStockedProduct):
                if product.quantity < quantity:
                    raise ValueError("Not enough in stock")


    def order(self, shopping_list):
        """calculates the total price in respect to the promotions and total shopping list"""
        self.validate_order(shopping_list)
        total_price = 0
        for product, quantity in shopping_list.items():
            total_price += product.buy(quantity)
        return f'Order costs: {total_price} dollars.'

