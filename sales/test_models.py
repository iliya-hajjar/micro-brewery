"""
These tests could be better by dividing one class to pass and fail.
"""
from schema import Order, OrderDetails


def test_new_order():
    product = Order(transaction_id=13124, user_id=1)
    assert product.user_id == 1
    assert product.transaction_id == 13124
    assert product.user_id != 2
    assert product.transaction_id != 13122


def test_new_order_details():
    supplier = OrderDetails(order_id=1, product_id=2, product_count=5)
    assert supplier.order_id == 1
    assert supplier.product_id == 2
    assert supplier.product_count == 5
    assert supplier.order_id != 4
    assert supplier.product_id != 3
    assert supplier.product_count != 10

