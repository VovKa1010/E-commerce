from src.base_class_me import BaseClassMe
from src.exception.zero_product_quantity import ZeroProductQuantity
from src.product.product import Product


class Order(BaseClassMe):
    product: Product
    count_buy: int
    total_cost: float

    def __init__(self, product, count_buy):
        try:
            if product.quantity <= 0:
                raise ZeroProductQuantity
            self.product = product
            self.count_buy = count_buy
            self.total_cost = self.product.price * count_buy
        except ZeroProductQuantity as e:
            print(e)
        else:
            print("Успешно создан заказ")
        finally:
            print("Обработка создания заказа завершена")

    def __str__(self):
        return f"Покупка {self.product.name}, количество: {self.count_buy} на сумму {self.total_cost}"
