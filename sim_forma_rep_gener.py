
total_value = 0

print("Enter info for 3 products:\n")
products = []

for i in range(3):
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    total = price * quantity
    total_value += total
    products.append((name, price, quantity, total))
    print()

# Print table
print("Product       Price   Quantity   Total")
for i in products:
    print(f"{i[0]:<14}{i[1]:<8.2f}{i[2]:<11}{i[3]:.2f}")

print("-" * 38)
print(f"{'TOTAL VALUE:':<33}{total_value:.2f}$\n")
