import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def start(best_buy):
    while True:
        print("    Store Menu")
        print("    ----------")
        print(
            f'1. List all products in store'
            f'\n2. Show total amount in store'
            f'\n3. Make an order'
            f'\n4. Quit'
        )
        try:
            action = int(input("Please choose a number: "))
        except:
            print("Invalid Input. Please try again.")
            continue

        if action == 1:
            print()
            for i, product in enumerate(best_buy.get_all_products()):
                print(f'{i}. {product.name:28}, Price: ${product.price:4}, Quantity: {product.quantity}')
            print()

        elif action == 2:
            print()
            print(f"Total amount: {best_buy.get_total_quantity()}")
            print()

        elif action == 3:
            shopping_list = []
            while True:
                try:
                    product_input = input("Which product # do you want? (or leave blank to finish): ")
                    if product_input == "":
                        print(best_buy.order(shopping_list))
                        break
                    product_num = int(product_input)
                    if 0 <= product_num < len(best_buy.products):
                        product_name = best_buy.products[product_num]
                    else:
                        print("Invalid product number")
                        continue

                except ValueError:
                    print("Invalid input. Please try again.")
                    continue

                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0.")
                        continue
                except ValueError:
                    print("Invalid amount. Please enter a valid quantity.")
                    continue
                shopping_list.append((product_name, quantity))
                print("Product added to list")

        elif action == 4:
            break


if __name__ == '__main__':
    start(best_buy)