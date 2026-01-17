price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

print("Lista produktów i ich ceny przed rabatem:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

total_before_discount = sum(price_list.values())
print(f"\nCałkowita wartość produktów przed rabatem: ${total_before_discount:.2f}")

discounted_price_list = {product: round(price * 0.9, 2) 
                         for product, price in price_list.items()}

print("\nLista produktów i ich ceny po rabacie (10%):")
for product, discounted_price in discounted_price_list.items():
    print(f"{product}: ${discounted_price:.2f}")

total_after_discount = sum(discounted_price_list.values())
print(f"\nCałkowita wartość produktów po rabacie: ${total_after_discount:.2f}")
