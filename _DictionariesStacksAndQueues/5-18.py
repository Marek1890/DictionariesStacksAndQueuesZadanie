import json

# Open the JSON file in read mode
with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

# Print dogs under 5 years old
for dog in dogs:
    if dog['age'] < 5:
        print(f"Name: {dog['name']}, Age: {dog['age']}")
