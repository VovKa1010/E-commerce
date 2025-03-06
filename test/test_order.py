import pytest
from src.order import Order
from test.test_product.test_product import product_1


@pytest.fixture()
def order1(product_1):
    return Order(product_1, 5)


def test_order_init(order1):
    assert order1.product.name == "1"
    assert order1.count_buy == 5
    assert order1.total_cost == 50


def test_order_str(order1):
    assert str(order1) == "Покупка 1, количество: 5 на сумму 50"
