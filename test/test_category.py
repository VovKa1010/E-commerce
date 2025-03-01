import pytest
from src.category import *
from test.test_product import product_appel, product_oranges


@pytest.fixture()
def category_fruits(product_appel, product_oranges):
    Category.category_count = 0
    Category.product_count = 0
    products = [product_appel, product_oranges]
    return Category("fruits", "fruits description", products)


def test_category_init(category_fruits):
    assert category_fruits.name == "fruits"
    assert category_fruits.description == "fruits description"
    assert category_fruits.products == "appel, 10 руб. Остаток: 15 шт.\noranges, 20 руб. Остаток: 5 шт.\n"
    assert category_fruits.category_count == 1
    assert category_fruits.product_count == 2


def test_category_str(category_fruits):
    assert str(category_fruits) == "fruits, количество продуктов: 20 шт."


def test_category_add_product(category_fruits, product_oranges):
    category_fruits.add_product(product_oranges)
    assert category_fruits.product_count == 3
    category_fruits.add_product(None)
    assert category_fruits.product_count == 3
