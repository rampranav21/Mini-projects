#Menu of the restaurant code
hotelmenu ={
    'Coffee':40,
    'Pizza':60,
    'Burger':65,
    'Chilly paneer':70,
    'Waffel':90,    
    'Lassi':30,
}

print("Welcome to 5 star Restaurant")
print("Coffee: Rs40\nPizza: Rs60\nBurger: Rs65\nChilly paneer: Rs70\nWaffel: Rs90\nLassi: Rs30,")

order_total=0

item_1 = input("Enter the item you want to take")
if item_1 in hotelmenu:
    order_total += hotelmenu[item_1]
    print(f"Your item{item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (YES/NO)")
if another_order == "YES":
    item_2=input("Enter the name of second item")
    if item_2 in hotelmenu:
        order_total += hotelmenu[item_2]
        print(f"Item{item_2} has been added to order")
    else:
        print(f"Ordered item{item_2} is not available!")
    
print(f"The total amount of your order{order_total}")

