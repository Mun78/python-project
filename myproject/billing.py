# Hotel Billing System

def display_menu():
    print("\nWelcome to the Hotel ")
    print("Menu:")
    print("1. Tea - ₹10")
    print("2. Coffee - ₹15")
    print("3. Sandwich - ₹50")
    print("4. Burger - ₹100")
    print("5. Pizza - ₹200")
    print("6. Exit\n")

def calculate_bill(order):
    prices = {
        "Tea": 10,
        "Coffee": 15,
        "Sandwich": 50,
        "Burger": 100,
        "Pizza": 200
    }
    total = 0
    print("\nYour Order:")
    print("-" * 20)
    for item, quantity in order.items():
        cost = prices[item] * quantity
        total += cost
        print(f"{item}: {quantity} x ₹{prices[item]} = ₹{cost}")
    print("-" * 20)
    print(f"Total Bill: ₹{total}")
    print("-" * 20)
    return total

def main():
    menu = {
        1: "Tea",
        2: "Coffee",
        3: "Sandwich",                  
        4: "Burger",
        5: "Pizza"
    }
    order = {}
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 6:
                print("\nThank you for visiting!")
                break
            elif choice in menu:
                quantity = int(input(f"Enter quantity for {menu[choice]}: "))
                if quantity <= 0:
                    print("Quantity should be greater than zero. Try again.")
                    continue
                item = menu[choice]
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
                    
            else:
                print("Invalid choice. Please select from the menu.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    if order:
        calculate_bill(order)

if __name__ == "__main__":
    main()
