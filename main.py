class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: [Product]
    count_category = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_category += 1
        Category.count_products += len(products)


if __name__ == "__main__":
    pr_1 = Product("g", "g", 3, 4)
    pr_2 = Product("h", "h", 5, 6)

    ct_1 = Category("t", "t", [pr_1, pr_2])
    ct_2 = Category("t", "t", [pr_2])

    print(ct_1.name)
    print(ct_1.count_products)
