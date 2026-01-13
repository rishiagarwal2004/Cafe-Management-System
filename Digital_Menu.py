def getValidInput(prompt):#Take valid input
    while True:
        try:
            userInput = int(input(prompt))
            if userInput < 0:
                raise ValueError
            return userInput
        except ValueError:
            print("Oops! It looks like you've entered an invalid value. Please re-enter a valid positive integer.")

# Welcome message
def welcomemsg():
    msg = "Welcome to the Rishi's cafe! Here's your menu:"
    print(msg)

# Display menu
def display_menu():
    print("\n--- Menu ---")
    menu = {
        "Pizza": 99, "Burger": 49, "Pasta": 50,
        "Noodles": 50, "Fried Rice": 50, "French Fries": 40,
        "Tea": 20, "Coffee": 30, "Cold Drink": 40,"Shakes":50,
        "Pastry":50, "Cookies":10, "Cake":300
    }  
    for item, price in menu.items():
        print(f"{item}: ₹{price}")
    return menu

# Option for choosing food
def choice(menu):
    choosing = []
    while True:
        item = input("Enter the item you want or type 'Done' to finish: ").strip().title()
        if item == "Done":
            break
        elif item in menu:
            quantity = getValidInput(f"Enter the quantity of {item}: ")
            choosing.append((item, quantity))
        else:
            print("Item not available, sorry.")
    print("Your order is placed:", choosing)
    return choosing

# Modify the order its a new feature
def modify_order(order, menu):
    print("\n--- Modify Order ---")
    while True:
        print("\nYour current order:")
        for item, quantity in order:
            print(f"{item} x{quantity}")
        action = input("Do you want to 'Add', 'Remove', or 'Done' to finalize your order? ").strip().title()
        if action == "Add":
            item = input("Enter the item to add: ").strip().title()
            if item in menu:
                quantity = getValidInput(f"Enter the quantity of {item}: ")
                order.append((item, quantity))
            else:
                print("Item not available.")
        elif action == "Remove":
            item = input("Enter the item to remove: ").strip().title()
            # Filter out the item to be removed
            order = list(filter(lambda x: x[0] != item, order))
        elif action == "Done":
            break
        else:
            print("Invalid option. Try again.")
    return order

# Calculate the bill
def bill(order, menu):
    print("\n--- Your Bill ---")
    # Using map() to calculate the cost of each item
    costs = list(map(lambda x: menu[x[0]] * x[1], order))#menu[x[0]]=retrive the food item from the menu dictionary
    total = sum(costs)#x[1]=quantity 

    # Print itemized bill
    for (item, quantity), cost in zip(order, costs):
        print(f"{item} x{quantity}: ₹{cost}")

    # Apply discount if applicable
    discount = 0
    if total > 500:  # 10% discount for orders above ₹500
        discount = total * 0.1
        print(f"Discount: ₹{discount:.2f}")
        total -= discount

    print(f"Total amount to pay: ₹{total:.2f}")

# Main function
def main():
    welcomemsg()
    menu = display_menu()
    order = choice(menu)
    if order:
        print("\nWould you like to modify your order?")
        modify = input("Type 'yes' to modify or 'no' to finalize: ").strip().lower()
        if modify == "yes":
            order = modify_order(order, menu)
        bill(order, menu)
    else:
        print("No items ordered. Thank you for visiting!")

main()
  