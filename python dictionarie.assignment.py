# -----------------------------------------
# Exercise 1: NumPy Arrays in Banking Sector
# -----------------------------------------
import numpy as np

print("\n--- Exercise 1: NumPy Arrays (Banking) ---")

# 1. Create 2D array (4 branches x 6 months)
transactions = np.array([
    [1200, 1300, 1250, 1400, 1350, 1500],   # Branch 1
    [1100, 1150, 1175, 1250, 1230, 1300],   # Branch 2
    [1500, 1600, 1550, 1650, 1700, 1750],   # Branch 3
    [1000, 1050, 1025, 1100, 1080, 1150]    # Branch 4
])

# 2. Total transactions per branch
total_per_branch = np.sum(transactions, axis=1)
print("Total transactions per branch:", total_per_branch)

# 3. Branch with highest total transactions
max_branch_index = np.argmax(total_per_branch)
print(f"Branch {max_branch_index + 1} has the highest total transactions.")

# 4. Average monthly transaction volume across all branches
average_monthly = np.mean(transactions, axis=0)
print("Average monthly transaction volume:", average_monthly)

# 5. Reshape to 3x8 and explain
reshaped = transactions.reshape(3, 8)
print("Reshaped array (3x8):\n", reshaped)
print("Note: Reshaping changes structure but not the data values.")

# -----------------------------------------
# Exercise 2: Lists in Logistics Management
# -----------------------------------------
print("\n--- Exercise 2: Python Lists (Logistics) ---")

# 1. Create a list of 10 delivery routes
routes = ["NorthLine", "EastExpress", "SouthHaul", "WestTrack", "CentralRoute",
          "NortheastLoop", "NorthPass", "SouthBound", "EastTrail", "MetroLink"]

# 2. Append new route and remove a discontinued one
routes.append("SkyRoute")
routes.remove("SouthBound")

# 3. Sort alphabetically and reverse
routes.sort()
routes.reverse()
print("Sorted & Reversed Routes:", routes)

# 4. Count routes starting with "N"
n_routes = [r for r in routes if r.startswith("N")]
print("Number of routes starting with 'N':", len(n_routes))

# 5. List comprehension for routes longer than 10 characters
long_routes = [r for r in routes if len(r) > 10]
print("Routes longer than 10 characters:", long_routes)

# -----------------------------------------
# Exercise 3: Tuples in Medical Records
# -----------------------------------------
print("\n--- Exercise 3: Python Tuples (Healthcare) ---")

# 1. Create patient tuple
patient = ("John Doe", 45, "120/80", 72)

# 2. Access and print age and heart rate
print("Patient Age:", patient[1])
print("Patient Heart Rate:", patient[3])

# 3. Explain why tuples are suitable
print("Reason: Tuples are immutable, ensuring patient data cannot be changed accidentally.")

# 4. Convert to list, update heart rate, back to tuple
patient_list = list(patient)
patient_list[3] = 75  # Updated heart rate
patient = tuple(patient_list)
print("Updated patient tuple:", patient)

# 5. Tuple of 5 patients and extract names
patients = (
    ("Alice Smith", 30, "110/70", 65),
    ("Bob Lee", 50, "130/85", 78),
    ("Cathy Tan", 28, "115/75", 70),
    ("David Kim", 60, "140/90", 80),
    ("Eva Liu", 35, "125/80", 72)
)

names = [p[0] for p in patients]
print("All patient names:", names)

# -----------------------------------------
# Exercise 4: Dictionaries in E-Commerce
# -----------------------------------------
print("\n--- Exercise 4: Python Dictionaries (E-Commerce) ---")

# 1. Create dictionary with 5 products and stock quantities
inventory = {
    "Laptop": 15,
    "Mouse": 50,
    "Keyboard": 30,
    "Monitor": 8,
    "Printer": 5
}

# 2. Add new product and update existing one
inventory["Tablet"] = 20
inventory["Monitor"] = 10

# 3. Function to return products with stock < 10
def low_stock_products(stock_dict):
    return [product for product, qty in stock_dict.items() if qty < 10]

print("Low stock products (<10):", low_stock_products(inventory))

# 4. Delete discontinued product and display updated inventory
del inventory["Printer"]
print("Updated inventory after removing 'Printer':", inventory)

# 5. Use .items() to loop through and print each product with quantity
print("Product Stock Levels:")
for product, qty in inventory.items():
    print(f"- {product}: {qty}")
