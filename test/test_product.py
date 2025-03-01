import pytest
from src.product import *


@pytest.fixture()
def product_1():
    return Product("1", "1 description", 10, 15)


@pytest.fixture()
def product_2():
    return Product("2", "2 description", 20, 5)


@pytest.fixture()
def smartphone():
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space")


@pytest.fixture()
def lawn_grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый")


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


def test_product_init(product_1):
    assert product_1.name == "1"
    assert product_1.description == "1 description"
    assert product_1.price == 10
    assert product_1.quantity == 15


def test_smartphone_init(smartphone):
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


def test_lawn_grass_init(lawn_grass):
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_product_str(product_1):
    assert str(product_1) == "1, 10 руб. Остаток: 15 шт."


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 250


def test_product_add_smartphone(smartphone):
    assert smartphone + smartphone == 3360000


def test_product_add_lawn_grass(lawn_grass):
    assert lawn_grass + lawn_grass == 20000


def test_product_add_lawn_grass_with_smartphone_exception(lawn_grass, smartphone):
    try:
        lawn_grass + smartphone
    except TypeError:
        assert True
    else:
        assert False


def test_product_price(product_1, monkeypatch):
    assert product_1.price == 10

    product_1.price = 15
    assert product_1.price == 15

    product_1.price = 0
    assert product_1.price == 15

    product_1.price = -10
    assert product_1.price == 15

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product_1.price = 10
    assert product_1.price == 15

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product_1.price = 10
    assert product_1.price == 10


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
