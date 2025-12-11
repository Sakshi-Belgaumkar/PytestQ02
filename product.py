# main.py

def format_product(product_id, name, quantity, price):
    """
    Accepts product details and returns a well-formatted string.
    """

    return (
        f"Product ID   : {product_id}\n"
        f"Name         : {name}\n"
        f"Quantity     : {quantity}\n"
        f"Price        : ₹{price}"
    )


# Example usage
if __name__ == "__main__":
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    print("\n--- Product Details ---")
    print(format_product(pid, name, qty, price))
