# Menu of the restaurant
hotel_menu = {
    'Coffee': 40,
    'Pizza': 60,
    'Burger': 65,
    'Chilly Paneer': 70,
    'Waffle': 90,    
    'Lassi': 30,
}

print("Welcome to 5-Star Restaurant")
print("Menu:")
for item, price in hotel_menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

while True:
    # Ask for an item to order
    item = input("Enter the item you want to order: ")
    if item in hotel_menu:
        order_total += hotel_menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Sorry, '{item}' is not available on the menu.")
    
    # Ask if they want to order another item
    another_order = input("Do you want to add another item? (YES/NO): ").strip().upper()
    if another_order != "YES":
        break

print(f"The total amount of your order is: Rs{order_total}")


