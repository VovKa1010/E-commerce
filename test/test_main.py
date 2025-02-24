import pytest
from main import *


@pytest.fixture()
def product_appel():
    return Product("appel", "appel description", 10, 15)


@pytest.fixture()
def product_oranges():
    return Product("oranges", "oranges description", 20, 5)


@pytest.fixture()
def category_fruits(product_appel, product_oranges):
    products = [product_appel, product_oranges]
    return Category("fruits", "fruits description", products)


def test_product_init(product_appel, product_oranges):
    assert product_appel.name == "appel"
    assert product_appel.description == "appel description"
    assert product_appel.price == 10
    assert product_appel.quantity == 15
    assert product_oranges.name == "oranges"
    assert product_oranges.description == "oranges description"
    assert product_oranges.price == 20
    assert product_oranges.quantity == 5


def test_category_init(category_fruits):
    assert category_fruits.name == "fruits"
    assert category_fruits.description == "fruits description"
    assert category_fruits.products[0].name == "appel"
    assert category_fruits.products[1].name == "oranges"
    assert category_fruits.count_category == 1
    assert category_fruits.count_products == 2
