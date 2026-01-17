def hotel_list(hotels):
    return ', '.join(hotel['name'] for hotel in hotels)

def avg_price(hotels):
    return round(sum(hotel['price'] for hotel in hotels) / len(hotels))

hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},
   {"name": "Metropol", "price": 480.00},
   {"name": "New Port", "price": 420.00},
   {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},
   {"name": "Aqua", "price": 345.00},
   {"name": "La Boutique", "price": 390.00},
   {"name": "Marina", "price": 410.00}
]

krakow_hotels = hotel_list(hotels_in_Krakow)
krakow_avg_price = avg_price(hotels_in_Krakow)

sopot_hotels = hotel_list(hotels_in_Sopot)
sopot_avg_price = avg_price(hotels_in_Sopot)

print(f"Hotels in Krakow: {krakow_hotels}")
print(f"Average hotel price in Krakow: {krakow_avg_price}")
print(f"Hotels in Sopot: {sopot_hotels}")
print(f"Average hotel price in Sopot: {sopot_avg_price}")

cheaper = []
if krakow_avg_price < sopot_avg_price:
    cheaper.append("Krakow")
if sopot_avg_price < krakow_avg_price:
    cheaper.append("Sopot")

if cheaper:
    print(f"Cheaper hotels in: {', '.join(cheaper)}")
else:
    print("Hotels are the same price in both cities")
