import json

# Load voting data from file
try:
    with open('vote.json', 'r') as file:
        vote_data = json.load(file)
except FileNotFoundError:
    vote_data = {}

# Get vote input
person_name = input('Name of the person you are voting for: ')

# Increment vote count or add new entry
if person_name in vote_data:
    vote_data[person_name] += 1
else:
    vote_data[person_name] = 1

# Save updated vote data to file
with open('vote.json', 'w') as file:
    json.dump(vote_data, file, indent=4)

print(f"Vote for {person_name} registered.")
