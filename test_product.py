# test_product.py

from product import format_product

def test_format_product():
    result = format_product("P101", "Notebook", 5, 45.50)

    expected = (
        "Product ID   : P101\n"
        "Name         : Notebook\n"
        "Quantity     : 5\n"
        "Price        : ₹45.5"
    )

    assert result == expected
