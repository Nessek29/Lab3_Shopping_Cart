# Autor = Simbil
# Date = 2025-01-26
# this program i've created is simulating a shopping cart where the user add different item.
# Inside the program we got input such as name of item, price, and quantity also the total price of the items.
def shopping_cart():
    print("Welcome to the Shopping Cart Program")

while True:
        try:
            num_items = int(input("How many items do you have? "))

            if num_items < 1:
                raise ValueError("Please enter at least 1 item.")

            break   # if the user enter the valid input exit the loop
        except ValueError:
             print("Invalid input! Please enter a number.")


    #listing the inputs
        items = []
        total_cost = 0
        for i in range(num_items):
           while True: # this statement is used to create infinite loop
            try:
                name = input("Enter the item's name:")
                price = float(input(f"Enter the price of {name}: "))
                quantity = int(input(f"Enter the quantity of {name}: "))
                if price < 0 or  quantity < 0:
                    raise ValueError("You must enter positives values for price and quantity.")
                break  # if the user enters a valid input, exit the loop.
            except ValueError: 
                print("Oups! This is not a number. Please try again.")

# calculating the total cost of items.
                items.append((name, price, quantity))
                total_cost += price * quantity
                print(f"\nTotal cost: ${total_cost:.2f}")

    # Applicable discount( if the total cost is more than $100, apply 10% discount)
if total_cost > 100:
        discount = total_cost * 0.10
        total_cost = total_cost - discount
        print(f"\nYou saved ${discount:.2f}  wit the 10% discount!.")
        print("\nDiscount Total is ${total_cost:.2f}.")

    # restarting the program
restart = input("\n Would like to shop again? (Yes/No): ")
if restart == "Yes":
        shopping_cart()
else:
            print("\nThank you for shopping with us!")


shopping_cart()


