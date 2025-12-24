grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}

price_egg = grocery_inventory["Eggs"][1]
if price_egg > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": ("Dairy", 4.50, 30)})
else:
    print("The price of Eggs is reasonable.")

# grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)}])
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

stock_milk = grocery_inventory["Milk"][2]
if stock_milk < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = ("Dairy", 3.50, 28)
else:
    print("Milk has sufficient stock")

if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price")

print("Updated inventory:", grocery_inventory)