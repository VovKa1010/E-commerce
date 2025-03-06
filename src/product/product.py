from src.product.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.price * self.quantity) + (other.price * other.quantity)

        raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                confirmation = input("Цена снижается. Подтвердите действие.(y)\n")
                if confirmation != "y":
                    return
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, new_product: dict, old_products: list = None):
        if old_products is None:
            return cls(**new_product)
        else:
            for old_product in old_products:
                if old_product["name"] == new_product["name"]:
                    new_product["quantity"] += old_product["quantity"]
                    if old_product["price"] > new_product["price"]:
                        new_product["price"] = old_product["price"]

            return cls(**new_product)
