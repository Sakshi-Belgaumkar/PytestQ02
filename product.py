# product.py

def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result


if __name__ == "_main_":
    # Sample input
    product_id = "P101"
    name = "Laptop"
    quantity = 5
    price = 55000

    print(product_details(product_id, name, quantity, price))
