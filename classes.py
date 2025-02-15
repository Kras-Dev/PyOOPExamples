from datetime import date
from enum import Enum

# Перечисление статусов заказа
class OrderStatus(Enum):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"

# Базовый класс товара
class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return f"Product: {self._name}, Price: {self._price}"

# Класс продукта питания
class FoodProduct(Product):
    def __init__(self, name: str, price: float, expiration_date: date, is_vegan: bool):
        super().__init__(name, price)
        self._expiration_date = expiration_date
        self._is_vegan = is_vegan

    def __str__(self):
        return f"{super().__str__()}, Expiration Date: {self._expiration_date.strftime('%d-%m-%Y')}, Is Vegan: {self._is_vegan}"

# Класс электроники
class ElectronicProduct(Product):
    def __init__(self, name: str, price: float, warranty_period: int, power_usage: float):
        super().__init__(name, price)
        self._warranty_period = warranty_period
        self._power_usage = power_usage

    def __str__(self):
        return f"{super().__str__()}, Warranty Period: {self._warranty_period} months, Power Usage {self._power_usage} W"

# Класс корзина
class Cart:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        self._products.remove(product)

    @property
    def get_total_price(self) -> float:
        return round(sum(product.price for product in self._products), 2)

    @property
    def products(self):
        return list(self._products)

# Класс заказ
class Order:
    def __init__(self, cart: Cart, phone_number: str):
        self._cart = cart
        self._phone_number = phone_number
        self._status = OrderStatus.PENDING

    def place_order(self):
        self._status = OrderStatus.SHIPPED

    def cancel_order(self):
        self._status = OrderStatus.CANCELED

    def __str__(self):
        return f"Order Status: {self._status.value}, Total Price: {self._cart.get_total_price}, Phone: {self._phone_number}"


if __name__ == "__main__":
    p = Product("soap", 2.22)
    print(p)
    p1 = FoodProduct("milk", 4.21, date(2026, 12, 31), False)
    print(p1)
    e = ElectronicProduct("TV", 99.99, 24, 90)
    c = Cart()
    c.add_product(p)
    c.add_product(p1)
    c.add_product(e)
    print(c.get_total_price)
    for product in c.products:
        print(product)
    order = Order(c, "123-456-78")
    print(order)
    order.place_order()
    print(order)

