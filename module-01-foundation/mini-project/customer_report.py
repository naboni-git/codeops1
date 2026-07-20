# List of customers stored as (name, balance) pairs
customers = [
    ("Almaz", 1500), 
    ("Dawit", 700), 
    ("Tigist", 200),
    ("Hanna", 1200), 
    ("Samuel", 450)
]

# Function to determine subscription tier based on balance
def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"

# Counters to keep track of how many customers are in each tier
premium_count = 0
standard_count = 0
basic_count = 0

print("--- TeleBirr Customer Report ---")
# Loop through customers, print their status, and count the tiers
for name, balance in customers:
    customer_tier = tier(balance)
    print(f"{name}: {customer_tier} ({balance} ETB)")
    
    # Increment the correct counter
    if customer_tier == "Premium":
        premium_count += 1
    elif customer_tier == "Standard":
        standard_count += 1
    elif customer_tier == "Basic":
        basic_count += 1

# Print the final summary report
print("\n--- Summary Report ---")
print(f"Premium Tier Customers: {premium_count}")
print(f"Standard Tier Customers: {standard_count}")
print(f"Basic Tier Customers: {basic_count}")
