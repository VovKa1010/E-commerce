class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
