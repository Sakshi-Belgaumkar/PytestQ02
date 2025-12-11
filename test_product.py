# test_product.py

from product import format_product

def test_format_product():
    result = format_product("P101", "Notebook", 5, 45.50)

    expected = (
        "Product ID   : P101"
        "Name         : Notebook"
        "Quantity     : 5"
        "Price        : ₹45.5"
    )

    assert product("P101", "Notebook", 5, 45.5) == expected_output
