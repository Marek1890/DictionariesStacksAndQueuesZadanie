products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

print("Lista produktów i ilość:")
for product, quantity in products.items():
    print(f"{product}: {quantity}")

number_of_products = len(products)
total_products = sum(products.values())

print("\nCałkowita liczba produktów w sklepie:", total_products )
print(f"Liczba produktów w sklepie: {number_of_products}")