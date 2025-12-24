prices = [29.99, 45.50, 12.75, 38.20]
discounts = [10, 20, 15, 5]

for index in range(len(prices)):
    prices[index] -= prices[index] * (discounts[index]/100)
    updated_price = prices[index]
    
    print(f"Updated price for item {index}: ${updated_price:.2f}")