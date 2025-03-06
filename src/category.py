from src.base_class_me import BaseClassMe
from src.exception.zero_product_quantity import ZeroProductQuantity
from src.product.product import *


class Category(BaseClassMe):
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):

        if not products:
            products = []

        for product in products:
            if not isinstance(product, Product):
                raise TypeError("Не все элементы списка products являются классом или наследником от Product")
            elif product.quantity <= 0:
                raise ZeroDivisionError

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        sum_products_quantity = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {sum_products_quantity} шт."

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product}\n"

        return result

    def add_product(self, product) -> None:
        try:
            if isinstance(product, Product):
                if product.quantity <= 0:
                    raise ZeroProductQuantity
                self.__products.append(product)
                Category.product_count += 1
            else:
                raise TypeError
        except ZeroProductQuantity as e:
            print(e)
        else:
            print("Успешно добавлен товар")
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self):
        try:
            sum_products = sum([product.price for product in self.__products])
            avg_price = sum_products / len(self.__products)
            return avg_price
        except ZeroDivisionError:
            return 0
