# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for index in range(len(prices)):
        revenue_index = prices[index] * quantities_sold[index]
        revenue.append(revenue_index)
    return revenue

def formatted_output(revenues):
    revenues_sorted = sorted(revenues)
    for revenue in revenues_sorted:
        print(f"{revenue[0]} has total revenue of ${revenue[1]}")

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = tuple(zip(products, revenue))
formatted_output(revenue_per_product)
