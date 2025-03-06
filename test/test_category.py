import pytest
from src.category import *
from test.test_product.test_product import product_1, product_2
from test.test_product.test_smartphone import smartphone
from test.test_product.test_lawn_grass import lawn_grass


@pytest.fixture()
def category(product_1, product_2):
    Category.category_count = 0
    Category.product_count = 0
    products = [product_1, product_2]
    return Category("category", "category description", products)


@pytest.fixture()
def category_without_products(product_1, product_2):
    Category.category_count = 0
    Category.product_count = 0
    return Category("category", "category description")


def test_category_init(category):
    assert category.name == "category"
    assert category.description == "category description"
    assert category.products == "1, 10 руб. Остаток: 15 шт.\n2, 20 руб. Остаток: 5 шт.\n"
    assert category.category_count == 1
    assert category.product_count == 2


def test_category_init_without_products(category_without_products):
    assert category_without_products.category_count == 1
    assert category_without_products.product_count == 0


def test_category_init_products_other_type(product_1):
    with pytest.raises(TypeError):
        Category.category_count = 0
        Category.product_count = 0
        products = [product_1, None]
        Category("category", "category description", products)


def test_category_init_products_quantity_zero(product_1, product_2):
    with pytest.raises(ZeroDivisionError):
        Category.category_count = 0
        Category.product_count = 0
        product_2.quantity -= product_2.quantity
        products = [product_1, product_2]
        Category("category", "category description", products)


def test_category_str(category):
    assert str(category) == "category, количество продуктов: 20 шт."


def test_category_add_product(capsys, category, product_1):
    category.add_product(product_1)
    assert category.product_count == 3
    message = capsys.readouterr()
    messages_split = message.out.strip().split('\n')
    assert messages_split[-2] == "Успешно добавлен товар"
    assert messages_split[-1] == "Обработка добавления товара завершена"


def test_category_add_product_smartphone(capsys, category, smartphone):
    category.add_product(smartphone)
    assert category.product_count == 3
    message = capsys.readouterr()
    messages_split = message.out.strip().split('\n')
    assert messages_split[-2] == "Успешно добавлен товар"
    assert messages_split[-1] == "Обработка добавления товара завершена"


def test_category_add_product_lawn_grass(capsys, category, lawn_grass):
    category.add_product(lawn_grass)
    assert category.product_count == 3
    message = capsys.readouterr()
    messages_split = message.out.strip().split('\n')
    assert messages_split[-2] == "Успешно добавлен товар"
    assert messages_split[-1] == "Обработка добавления товара завершена"


def test_category_add_product_quantity_zero(capsys, category, product_1):
    product_1.quantity -= product_1.quantity
    category.add_product(product_1)
    message = capsys.readouterr()
    messages_split = message.out.strip().split('\n')
    assert messages_split[-2] == "Количество продукта не должно быть 0"
    assert messages_split[-1] == "Обработка добавления товара завершена"


def test_category_add_product_none(category):
    with pytest.raises(TypeError):
        category.add_product(None)


def test_category_middle_price(category):
    assert category.middle_price() == 15


def test_category_middle_price_without_products(category_without_products):
    assert category_without_products.middle_price() == 0
