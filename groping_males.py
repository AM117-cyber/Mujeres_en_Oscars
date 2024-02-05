import json

# Load the JSON file
with open('tonys1.json', 'r') as f:
    data = json.load(f)

# Extract male staff members
male_staff_members = {}
for year, categories in data.items():
    for category, staff in categories.items():
        for staff_member, details in staff.items():
            if details.get('gender') == 'male':
                if year not in male_staff_members:
                    male_staff_members[year] = {}
                if category not in male_staff_members[year]:
                    male_staff_members[year][category] = {}
                male_staff_members[year][category][staff_member.lower()] = details

# Write to JSON
with open('male_staff_members.json', 'w') as f:
    json.dump(male_staff_members, f, indent=4)
