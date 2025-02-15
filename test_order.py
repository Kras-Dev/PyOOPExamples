import pytest
from datetime import date
from classes import Product, FoodProduct, ElectronicProduct, Cart, Order, OrderStatus

def test_product_initialization():
    product = Product("Test Product", 10.0)
    assert product.name == "Test Product"
    assert product.price == 10.0

def test_food_product_initialization():
    food_product = FoodProduct("Test Food", 5.0, date(2026, 12, 31), True)
    assert food_product.name == "Test Food"
    assert food_product.price == 5.0
    assert food_product._expiration_date == date(2026, 12, 31)
    assert food_product._is_vegan is True

def test_electronic_product_initialization():
    electronic_product = ElectronicProduct("Test Gadget", 150.0, 12, 50.0)
    assert electronic_product.name == "Test Gadget"
    assert electronic_product.price == 150.0
    assert electronic_product._warranty_period == 12
    assert electronic_product._power_usage == 50.0

def test_cart_add_product():
    cart = Cart()
    product = Product("Test Product", 10.0)
    cart.add_product(product)
    assert len(cart.products) == 1
    assert cart.get_total_price == 10.0

def test_cart_remove_product():
    cart = Cart()
    product = Product("Test Product", 10.0)
    cart.add_product(product)
    assert len(cart.products) == 1
    cart.remove_product(product)
    assert len(cart.products) == 0
    assert cart.get_total_price == 0.0

def test_order_place():
    cart = Cart()
    product = Product("Test Product", 10.0)
    cart.add_product(product)
    order = Order(cart, "123-456-78")
    order.place_order()
    assert order._status == OrderStatus.SHIPPED

def test_order_cancel():
    cart = Cart()
    product = Product("Test Product", 10.0)
    cart.add_product(product)
    order = Order(cart, "123-456-78")
    order.cancel_order()
    assert order._status == OrderStatus.CANCELED