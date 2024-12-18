#displays the list of food items along with their prices.
def display_menu(menu):
    """Display the food menu."""
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item}: Php{price:.2f}")

#Allows the user to select multiple items from the menu and how many.
def get_order(menu):
    """Prompt the user to select items from the menu."""
    order = {}
    while True:
        choice = input("\nEnter the name of the food item you want to order (or type 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        if choice in menu:
            quantity = input(f"Enter the quantity for {choice}: ").strip()
            try:
                quantity = int(quantity)
                if quantity > 0:
                    if choice in order:
                        order[choice] += quantity
                    else:
                        order[choice] = quantity
                else:
                    print("Quantity must be a positive integer.")
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
        else:
            print("Invalid choice. Please select an item from the menu.")
    return order


#calculates the total cost of the user's order and displays a summary.
def calculate_total(order, menu):
    """Calculate the total cost of the selected items."""
    total = 0
    print("\n--- Order Summary ---")
    for item, quantity in order.items():
        cost = menu[item] * quantity
        total += cost
        print(f"{item} x{quantity}: Php{cost:.2f}")
    print(f"\nThe total cost is: Php{total:.2f}")
    return total


#payment and calculates change.
def process_payment(total):
    """Process the payment from the user."""
    while True:
        try:
            cash = float(input("\nEnter the amount of cash rendered: "))
            if cash >= total:
                change = cash - total
                print(f"Payment successful! Your change is: Php{change:.2f}")
                break
            else:
                print("Insufficient cash. Please provide enough to cover the total cost.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

#The entry point of the program.
if __name__ == "__main__":
    menu = {
        "Kwek-Kwek": 25,
        "Fishball": 15,
        "Kikiam": 15,
        "Gulaman": 12,
        "Isaw": 5
    }

    display_menu(menu)
    order = get_order(menu)
    total_cost = calculate_total(order, menu)
    process_payment(total_cost)
