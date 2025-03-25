import pytest
from products import Product

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
