import json  # Dodaj ten import na początku programu

favorite = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954,
    "genre": "Fantasy",
    "rating": 9.3
}

# Save the favorite book/film data to a JSON file
with open('favorite.json', 'w') as file:
    json.dump(favorite, file, indent=4)

print("Favorite data has been written to favorite.json")
