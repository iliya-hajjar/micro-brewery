"""
These tests could be better by dividing one class to pass and fail.
"""
from .schema import Product, Supplier, Category


def test_new_product():
    product = Product(name="lorem", price=1.22, brand="ipsum", count=10,
                      location="26985 Brighton Lane,Lake Forest, CA 92630", description="", category_id=1, supplier_id=2)
    assert product.name == 'lorem'
    assert product.price == 1.22
    assert product.brand == 'ipsum'
    assert product.count == 10
    assert product.location == '26985 Brighton Lane,Lake Forest, CA 92630'
    assert product.category_id == 1
    assert product.supplier_id != 1


def test_new_supplier():
    supplier = Supplier(name='FOO', address='26985 Brighton Lane,Lake Forest, CA 92630', category_id=1)
    assert supplier.name == 'FOO'
    assert supplier.address != '16985 Brighton Lane,Lake Forest, CA 92630'
    assert supplier.category_id == 1


def test_new_category():
    category = Category(name="healthcare")
    assert category.name == 'healthcare'
