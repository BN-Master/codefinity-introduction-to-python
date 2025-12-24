# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started...")
for item, value in inventory.items():
    print(f"Processing {item}")
    while value[0] < value[1]:
        value[0] += value[2]
        if value[0] > discount_threshold:            
            value[3] = True
print("Processing completed")