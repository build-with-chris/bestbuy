import products
import store

# inital inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
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
            ValueError("Invalid Input")
            continue

        if action == 1:
            for product in best_buy.get_all_products():
                print(product.name, product.price, product.quantity)
        if action == 2:
            print(f"Total amount: {best_buy.get_total_quantity()}")

        if action == 3:
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            shopping_list = (product_name, quantity)
            best_buy.order(shopping_list)
        if action == 4:
            break






if __name__ == '__main__':
    start(best_buy)

