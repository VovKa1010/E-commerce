from src.product.product import *


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):

        for product in products:
            if not isinstance(product, Product):
                raise TypeError("Не все элементы списка products являются классом или наследником от Product")

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        sum_products_quantity = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {sum_products_quantity} шт."

    def add_product(self, product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product}\n"

        return result
