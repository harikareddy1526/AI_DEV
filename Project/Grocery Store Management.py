'''
add product
view products
search product
update stock
sell product
view total sales
delete product
exit
'''
import json
products = []
sales = 0
def save_data():
    with open("grocery.json", "w") as f:
        json.dump(products, f)

def load_data():
    global products
    try:
        with open("grocery.json", "r") as f:
            products = json.load(f)
    except FileNotFoundError:
        products = []

def add_product():
    name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists.")
            return

    product = {
        "name": name,
        "id": product_id,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    save_data()
    print("Product added successfully!")

def view_products():
    if len(products) == 0:
        print("No products found.")
    else:
        for product in products:
            print("================")
            print("Name:", product["name"])
            print("ID:", product["id"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

def search_product():
    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("================")
            print("Name:", product["name"])
            print("ID:", product["id"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
            return

    print("Product not found.")

def update_stock():
    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:
            quantity = int(input("Enter quantity to add: "))

            product["quantity"] += quantity
            save_data()

            print("Stock updated successfully!")
            print("New quantity:", product["quantity"])
            return

    print("Product not found.")

def sell_product():
    global sales

    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:

            quantity = int(input("Enter quantity to sell: "))

            if quantity > product["quantity"]:
                print("Not enough stock available.")
                return

            product["quantity"] -= quantity

            total = quantity * product["price"]
            sales += total

            save_data()

            print("Product sold successfully!")
            print("Total amount:", total)
            print("Remaining quantity:", product["quantity"])
            return

    print("Product not found.")

def view_total_sales():
    print("================")
    print("Total sales:", sales)

def delete_product():
    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_data()

            print("Product deleted successfully!")
            return

    print("Product not found.")

def main():
    load_data()

    while True:
        print("\nGrocery Store Management Menu:")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Sell Product")
        print("6. View Total Sales")
        print("7. Delete Product")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            sell_product()

        elif choice == "6":
            view_total_sales()

        elif choice == "7":
            delete_product()

        elif choice == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
main()