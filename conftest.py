import pytest
from datetime import date
from classes import Product, FoodProduct, ElectronicProduct, Cart, Order

@pytest.fixture
def product():
    return Product("Sample Product", 10.0)

@pytest.fixture
def food_product():
    return FoodProduct("Sample Food", 5.0, date(2026, 12, 31), True)

@pytest.fixture
def electronic_product():
    return ElectronicProduct("Sample Electronic", 20.0, 12, 150.0)

@pytest.fixture
def cart():
    return Cart()

@pytest.fixture
def order(cart):
    return Order(cart, "123-456-78")