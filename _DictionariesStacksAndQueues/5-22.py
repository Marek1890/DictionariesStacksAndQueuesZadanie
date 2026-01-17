import json

# Zbieramy dane o produkcie z klawiatury
product = {}

product['name'] = input("Enter the product name: ")
product['price'] = float(input("Enter the price (in PLN): "))
product['paid'] = input("Paid (yes/no): ").strip().lower() == 'yes'

# Zapisujemy dane produktu do pliku JSON
with open('product.json', 'w') as file:
    json.dump(product, file, indent=4)

print("Product data has been written to product.json")
