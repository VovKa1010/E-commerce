import pytest
from src.order import Order
from test.test_product.test_product import product_1


@pytest.fixture()
def order1(product_1):
    return Order(product_1, 5)


def test_order_init(capsys, order1):
    assert order1.product.name == "1"
    assert order1.count_buy == 5
    assert order1.total_cost == 50
    message = capsys.readouterr()
    messages_split = message.out.strip().split('\n')
    assert messages_split[-2] == "Успешно создан заказ"
    assert messages_split[-1] == "Обработка создания заказа завершена"


def test_order_init_product_zero_quantity(capsys, product_1):
    product_1.quantity -= product_1.quantity
    Order(product_1, 1)
    message = capsys.readouterr()
    messages_split = message.out.strip().split('\n')
    assert messages_split[-2] == "Количество продукта не должно быть 0"
    assert messages_split[-1] == "Обработка создания заказа завершена"


def test_order_str(order1):
    assert str(order1) == "Покупка 1, количество: 5 на сумму 50"
