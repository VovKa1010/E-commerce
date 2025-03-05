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


def test_category_init(category):
    assert category.name == "category"
    assert category.description == "category description"
    assert category.products == "1, 10 руб. Остаток: 15 шт.\n2, 20 руб. Остаток: 5 шт.\n"
    assert category.category_count == 1
    assert category.product_count == 2


def test_category_init_exception(product_1):
    with pytest.raises(TypeError):
        Category.category_count = 0
        Category.product_count = 0
        products = [product_1, None]
        Category("category", "category description", products)


def test_category_str(category):
    assert str(category) == "category, количество продуктов: 20 шт."


def test_category_add_product(category, product_1):
    category.add_product(product_1)
    assert category.product_count == 3


def test_category_add_product_smartphone(category, smartphone):
    category.add_product(smartphone)
    assert category.product_count == 3


def test_category_add_product_lawn_grass(category, lawn_grass):
    category.add_product(lawn_grass)
    assert category.product_count == 3


def test_category_add_product_exception(category):
    with pytest.raises(TypeError):
        category.add_product(None)
