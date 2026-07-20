# Pharmacy Inventory Tracker

stock = {}

# Read stock.txt
try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, quantity = line.strip().split(",")
            stock[item] = int(quantity)

except FileNotFoundError:
    print("stock.txt was not found. Starting with empty stock.")


# Add or subtract an item's quantity
def update_quantity(item, amount):
    stock[item] = stock.get(item, 0) + amount


# Add 5 Paracetamol
update_quantity("Paracetamol", 5)

# Subtract 2 Amoxicillin
update_quantity("Amoxicillin", -2)


# Find items with quantity below 10
low_stock = [item for item, quantity in stock.items() if quantity < 10]

print("Updated stock:")
for item, quantity in stock.items():
    print(f"{item}: {quantity}")

print("Low-stock items:", low_stock)


# Save the updated stock back to stock.txt
with open("stock.txt", "w") as file:
    for item, quantity in stock.items():
        file.write(f"{item},{quantity}\n")
