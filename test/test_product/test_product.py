import pytest
from src.product.product import Product


@pytest.fixture()
def product_1():
    return Product("1", "1 description", 10, 15)


@pytest.fixture()
def product_2():
    return Product("2", "2 description", 20, 5)


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


def test_product_str(product_1):
    assert str(product_1) == "1, 10 руб. Остаток: 15 шт."


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 250


def test_product_add_exception(product_1, product_2):
    with pytest.raises(TypeError):
        product_1 + 0


def test_product_price(capsys, monkeypatch, product_1):
    assert product_1.price == 10

    product_1.price = 15
    assert product_1.price == 15

    product_1.price = 0
    assert product_1.price == 15
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_1.price = -10
    assert product_1.price == 15
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

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
