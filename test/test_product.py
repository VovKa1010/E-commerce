import pytest
from src.product import *


@pytest.fixture()
def product_appel():
    return Product("appel", "appel description", 10, 15)


@pytest.fixture()
def product_oranges():
    return Product("oranges", "oranges description", 20, 5)


@pytest.fixture()
def new_product_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }


@pytest.fixture()
def old_products_list():
    return [
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 150000.0,
            "quantity": 8
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        },
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 220000.0,
            "quantity": 2
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        }
    ]


def test_product_init(product_appel, product_oranges):
    assert product_appel.name == "appel"
    assert product_appel.description == "appel description"
    assert product_appel.price == 10
    assert product_appel.quantity == 15
    assert product_oranges.name == "oranges"
    assert product_oranges.description == "oranges description"
    assert product_oranges.price == 20
    assert product_oranges.quantity == 5


def test_product_str(product_appel, product_oranges):
    assert str(product_appel) == "appel, 10 руб. Остаток: 15 шт."
    assert str(product_oranges) == "oranges, 20 руб. Остаток: 5 шт."


def test_product_add(product_appel, product_oranges):
    assert product_appel + product_oranges == 250


def test_product_price(product_appel, monkeypatch):
    assert product_appel.price == 10

    product_appel.price = 15
    assert product_appel.price == 15

    product_appel.price = 0
    assert product_appel.price == 15

    product_appel.price = -10
    assert product_appel.price == 15

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product_appel.price = 10
    assert product_appel.price == 15

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product_appel.price = 10
    assert product_appel.price == 10


def test_new_product(new_product_dict, old_products_list):
    pr_1 = Product.new_product(new_product_dict)
    assert pr_1.name == "Samsung Galaxy S23 Ultra"
    assert pr_1.description == "256GB, Серый цвет, 200MP камера"
    assert pr_1.price == 180000
    assert pr_1.quantity == 5
    pr_2 = Product.new_product(new_product_dict, old_products_list)
    assert pr_2.name == "Samsung Galaxy S23 Ultra"
    assert pr_2.description == "256GB, Серый цвет, 200MP камера"
    assert pr_2.price == 220000
    assert pr_2.quantity == 15
