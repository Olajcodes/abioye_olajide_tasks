# #  Super Market Price List
market_price_list = {}

items_list = ["Bag", "Jam", "Car", "Mat"]

for item in items_list:
    prices = float(input(f"Enter price for {item}: ")) 
    market_price_list[item] = prices

for item in market_price_list.keys():
    print(f"{item}: {market_price_list[item]}" )

market_price_list.update({"Jam": 100})      # Updating price

print(f"The updated price in the market list is {market_price_list}")
