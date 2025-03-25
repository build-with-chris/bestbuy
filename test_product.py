import pytest
from products import Product
import products
import store

def test_normal():
    assert Product("MacBook", price=1450, quantity=100)

def test_empty_name():
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

def test_negative_price():
    with pytest.raises(Exception):
         Product("MacBook Air M2", price=-10, quantity=100)

def test_inactive_product():
    assert Product("MacBook Air M2", price=1450, quantity=0).is_active() == False

def test_change_quantity():
    product1 =  Product("MacBook Air M2", price=10, quantity=100)
    product1.buy(50)
    assert product1.quantity == 50

def test_buy_more_than_storage():
    product1 = Product("MacBook Air M2", price=10, quantity=100)
    with pytest.raises(Exception):
        product1.buy(500)

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = store.Store(product_list)

def test_non_stocked():
    license = products.NonStockedProduct("Windows License", price=125)
    assert license.quantity == 0
    assert license.buy() == "The total price for your Windows License is 125"
    # assert license.show() == "Windows License, Price: 125"

def test_limited_product():
    shipping = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(Exception):
        shipping.buy(2)