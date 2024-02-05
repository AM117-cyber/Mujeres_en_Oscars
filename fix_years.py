import json

# Load your JSON file
with open('oscar_general.json', 'r') as f:
    data = json.load(f)

# Create a new dictionary with years incremented by 1
new_oscar_data = {str(int(year) + 1): data[year] for year in data}

# Replace the old oscar data with the new data
data = new_oscar_data

# Save the updated JSON data back to the file
with open('oscar_general.json', 'w') as f:
    json.dump(data, f, indent=4)
