import json

# Open the JSON file in read mode
with open('cities.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Print the JSON data
for city in data:
    for key, value in city.items():
        print(f"{key}: {value}")
    print()
