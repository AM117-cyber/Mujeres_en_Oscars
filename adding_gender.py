# import json

# def update_gender(tonys_file, oscar_file, output_file):
#     # Load the data from the tonys file
#     with open(tonys_file, 'r') as f:
#         all_nominees = json.load(f)
    
#     # Load the data from the oscar file
#     with open(oscar_file, 'r') as f:
#         female_nominees = json.load(f)
    
#     # Get a set of all female staff member names from the oscar file
#     females = set()
#     for year, categories in female_nominees.items():
#         for category, staff_members in categories.items():
#             for staff_member in staff_members.keys():
#                 females.add(staff_member.lower())
    
#     # Update the gender property of the staff members in the tonys file
#     for year, categories in all_nominees.items():
#         for category, staff_members in categories.items():
#             for staff_member in staff_members.keys():
                
#                 if staff_member.lower() in females:
#                     all_nominees[year][category][staff_member]['gender'] = 'female'
    
#     # Write the updated data to the output file
#     with open(output_file, 'w') as f:
#         json.dump(all_nominees, f, indent=4)

# # Call the function
# update_gender('tonys1.json', 'oscar_general.json', 'tonys1.json')



##############
##adding gender
##############
import json

# Load the data from the JSON files
with open('awards_all.json', 'r') as f:
    all_nominees = json.load(f)

with open('oscar_general.json', 'r') as f:
    female_nominees = json.load(f)

# Create a set of all female staff members
female_staff = set()
for year, categories in female_nominees.items():
    for category, staff_members in categories.items():
        for staff_member in staff_members.keys():
            if female_nominees[year][category][staff_member]['gender'] == 'male':
                female_staff.add(staff_member)

# Iterate over the data in file1 and add the gender property
print(female_staff)
for year, awards in all_nominees.items():
    for award, categories in awards.items():
        for category, staff_members in categories.items():
            for staff_member in staff_members.keys():
                print(staff_member)
                if staff_member in female_staff:
                
                    all_nominees[year][award][category][staff_member]['gender'] = 'male'

# Write the modified data back to the JSON file
with open('awards_all.json', 'w') as f:
    json.dump(all_nominees, f, indent=4)
