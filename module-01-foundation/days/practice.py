# =========================================================
# EXERCISE 1: Temperature label
# =========================================================
print("--- Exercise 1: Temperature label ---")
temp_input = input("Enter temperature in °C: ")
temp = int(temp_input)  # Converting input string to integer

if temp < 15:
    print("cold")
elif 15 <= temp <= 28:
    print("warm")
else:
    print("hot")
print()  # Empty line for spacing


# =========================================================
# EXERCISE 2: Receipt loop
# =========================================================
print("--- Exercise 2: Receipt loop ---")
for i in range(1, 11):
    print(f"Receipt #{i}")
print()


# =========================================================
# EXERCISE 3: Even numbers
# =========================================================
print("--- Exercise 3: Even numbers ---")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
print()


# =========================================================
# EXERCISE 4: Discount function
# =========================================================
print("--- Exercise 4: Discount function ---")
def apply_discount(price, percent=10):
    discount_amount = price * (percent / 100)
    return price - discount_amount

# Testing the function with and without default value
print(f"Original: 100 ETB, Discounted (default 10%): {apply_discount(100)} ETB")
print(f"Original: 200 ETB, Discounted (custom 20%): {apply_discount(200, 20)} ETB")
print()


# =========================================================
# EXERCISE 5: Countdown
# =========================================================
print("--- Exercise 5: Countdown ---")
count = 5
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!")
