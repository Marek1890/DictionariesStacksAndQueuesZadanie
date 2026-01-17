import json

# Open the JSON file in read mode
with open('computer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Print the JSON data
for key, value in data.items():
    print(f"{key}: {value}")
