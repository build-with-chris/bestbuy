import products
import store
import promotions

# setup initial stock of inventory
# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", 30)

best_buy = store.Store(product_list)


# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


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
            for i, product in enumerate(best_buy.get_all_products(),1):
                if hasattr(product, 'promotion'):
                    print(f'{i}. {product.name:28}, Price: ${product.price:4}, Quantity: {product.quantity}, Promotion: {product.promotion.description}')
                else:
                    print(
                        f'{i}. {product.name:28}, Price: ${product.price:4}, Quantity: {product.quantity}, Promotion: None')
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
                    if 1 <= product_num < len(best_buy.products)+1:
                        product_name = best_buy.products[product_num -1]
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