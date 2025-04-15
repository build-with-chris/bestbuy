from idlelib.mainmenu import menudefs

import products
import store
import promotions
from test_product import best_buy


def setup_store():
    """inital store setup with products and promotions"""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        products.Product("Google Pixel 7", price=500, quantity=250),
                        products.NonStockedProduct("Windows License", price=125),
                        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                        ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", 30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    return store.Store(product_list)


def start(store_obj):
    """depending on the users choice, the user can display, or buy items from the shop"""
    while True:
        action = display_menu()
        if action == 1:
            display_prodcuts_with_details(store_obj)

        elif action == 2:
            print(f"\nTotal amount: {store_obj.get_total_quantity()}")

        elif action == 3:
            """initializing a shoppinglist as dictionary and making the order
            when the user leaves the input field blank"""
            display_prodcuts_with_details(store_obj)
            shopping_list = {}
            while True:
                product_input = input("Which product # do you want? (or leave blank to finish): ")
                if product_input == "":
                    try:
                        print(store_obj.order(shopping_list))
                        break
                    except ValueError as e:
                        print(e)
                        break
                try:
                    product_num = int(product_input)
                    if 1 <= product_num < len(store_obj.products)+1:
                        product_name = store_obj.products[product_num -1]
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0.")
                        continue
                    if product_name in shopping_list:
                        shopping_list[product_name] += quantity
                    else:
                        shopping_list[product_name] = quantity
                    print("Product added to list")
                except ValueError:
                    break

        elif action == 4:
            print("Bye")
            break


def display_menu():
    """A simple shop menu as shown in Codio"""
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
        display_menu()
    return action


def display_prodcuts_with_details(store_obj):
    """A for loop that handles the different specifications regarding quantity of the products
    and their promotion"""
    print("-----")
    for i, product in enumerate(store_obj.get_all_products(), 1):
        if isinstance(product, products.LimitedProduct):
            quantity_display = "Limited to 1 per order!"
        elif isinstance(product, products.NonStockedProduct):
            quantity_display = "unlimited"
        else:
            quantity_display = f"Quantity: {product.quantity}"

        if hasattr(product, 'promotion'):
            print(
                f'{i}. {product.name:28}, Price: ${product.price:4}, '
                f'{quantity_display}, Promotion: {product.promotion.description}')
        else:
            print(f'{i}. {product.name:28}, Price: ${product.price:4}, '
                  f'{quantity_display}, Promotion: None')
    print("-----")


def main():
    BEST_BUY = setup_store()
    start(BEST_BUY)


if __name__ == "__main__":
    main()