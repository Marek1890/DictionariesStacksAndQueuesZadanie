import csv

# Map of first letter of registration plates to provinces
province_map = {
    'A': 'Dolnośląskie', 'B': 'Mazowieckie', 'C': 'Lubelskie', 'D': 'Małopolskie',
    'E': 'Podlaskie', 'F': 'Opolskie', 'G': 'Śląskie', 'H': 'Łódzkie',
    'I': 'Pomorskie', 'J': 'Wielkopolskie', 'K': 'Zachodniopomorskie', 'L': 'Lubuskie',
    'M': 'Podkarpackie', 'N': 'Kujawsko-pomorskie', 'O': 'Świętokrzyskie',
    'P': 'Warmia-Mazury', 'R': 'Mazowieckie', 'S': 'Lubusz'
}

# Read vehicle registration plates from file
with open('vehicle.txt', 'r') as file:
    plates = file.readlines()

# Count vehicles in each province
vehicle_count = {province: 0 for province in province_map.values()}

for plate in plates:
    letter = plate.strip()[0].upper()
    province = province_map.get(letter)
    if province:
        vehicle_count[province] += 1

# Print vehicle count for each province
for province, count in vehicle_count.items():
    print(f"{province}: {count} vehicles")
