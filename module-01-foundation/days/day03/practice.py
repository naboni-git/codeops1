# Exercise 1: Unique cities

cities = ["Addis Ababa", "Bahir Dar", "Addis Ababa", "Hawassa", "Bahir Dar"]

unique_cities = set(cities)

print("Unique cities:", unique_cities)
print("Number of unique cities:", len(unique_cities))


# Exercise 2: Price report

prices = {
    "Bread": 50,
    "Milk": 80,
    "Rice": 120,
    "Sugar": 100,
    "Coffee": 200
}

for item, price in prices.items():
    print(f"{item}: {price} ETB")


# Exercise 3: Tax comprehension

prices = [100, 250, 400, 80]

prices_with_tax = [price * 1.15 for price in prices]

print("Prices with 15% tax:", prices_with_tax)


# Exercise 4: Cheap items

cheap_items = [price for price in prices if price < 200]

print("Prices under 200:", cheap_items)


# Exercise 5: Write and read

names = ["Naboni", "Almaz", "Dawit"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())


# Exercise 6: Safe division

try:
    number = float(input("Enter a number: "))
    result = 1000 / number
    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
