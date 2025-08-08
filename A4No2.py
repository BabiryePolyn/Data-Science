# Original dictionary of product prices
prices = {'apple': 0.50, 'banana': 0.25, 'orange': 0.60}

print("Original product prices:")
print(prices)

# Increase the price of 'apple' by 10%
prices['apple'] = prices['apple'] * 1.10  # Multiply by 1.10 to increase by 10%
print("\nAfter increasing apple price by 10%:")
print(prices)

# Add a new product 'mango' with a price of 1.25
prices['mango'] = 1.25
print("\nAfter adding mango:")
print(prices)

# Display final prices with better formatting
print("\nFinal product prices:")
for product, price in prices.items():
    print(f"{product}: ${price:.2f}")