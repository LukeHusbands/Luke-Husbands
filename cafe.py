# Create list of items
menu = ["coffee", "hot chocolate", "tuna sandwich", "cinnamon swirl"]

# Create a dictionary with items from list as key and number of items in stock as value
stock = {
    "coffee": 20,
    "hot chocolate": 40,
    "tuna sandwich": 70,
    "cinnamon swirl": 30
}

# Create a dictionary with items from list as key and price of items as value
price = {
    "coffee": 4,
    "hot chocolate": 3.5,
    "tuna sandwich": 5.5,
    "cinnamon swirl": 3
}

# Initialize total stock value
total_stock = 0

# Calculate total stock value using for loop
for item in menu:
    total_stock += stock[item] * price[item]

# Print total stock value
print(total_stock)
