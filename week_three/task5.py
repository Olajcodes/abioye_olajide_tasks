#  Store Inventory Update

store = {"Book": 20, "Bag": 15, "Pen": 10}

print("The available items to buy include Bag, Book and Pen")

item_to_buy = input("Kindly provide what you want to buy: ").title()

quantity_of_item = int(input(f"Enter the quantity of {item_to_buy} to buy: "))

print(f"Before purchase: {store}")

store[item_to_buy] -= quantity_of_item

print(f"After purchase: {store}")