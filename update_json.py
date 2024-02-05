import json

# Load your JSON file
with open('em.json', 'r') as f:
    data = json.load(f)

# Function to capitalize each word in a string
def capitalize_name(name):
    return ' '.join(word.capitalize() for word in name.split(' '))

# Iterate over the JSON data and update the names
for year in data:
    for category in data[year]:
        for staff_member in list(data[year][category]):  # Create a copy of the keys
            capitalized_name = capitalize_name(staff_member)
            data[year][category][capitalized_name] = data[year][category].pop(staff_member)

# Save the updated JSON data back to the file
with open('emmys_complete.json', 'w') as f:
    json.dump(data, f, indent=4)

# import json

# # List of names
# names = ["peter ", "david ", "john ", "matthew ", "paul ", "george ", "michael ", "nick ", "tony ","jeremy ", "steve ", "steven ", "don ", "jared ", "zack ", "tyler ", "nick ", "duncan ", "duke ", "rupert ", "jacob ", "bernard ", "mac ", "hans ", "dennis ", "julio ", "arthur ", "darren ", "dustin ", "maurizio ", "chase ", "lin-manuel ", "joshua ", "gordon ", "gavin ", "gerard ", "gabe ", "sam ", "armando ", "kyle ", "colton ", "graham ", "dicky ", "bucky ", "hamish ", "patrick ", "derek ", "thom ", "miles ", "ethan ", "benjamin ", "pete ", "johnny ", "abel ", "alec ", "max ", "eli ", "lorne michaels", "sebastian ", "bobby ", "dale ", "opus moreschi", "wyatt ", "miguel ", "jake ", "jerry ", "elliott ", "gideon ", "fred ", "zach ", "eric ", "erik ", "colin ", "billy ", "jay ", "stuart ", "ben ", "justin ", "jorma taccone", "andy samberg", "daniel ", "lee ", "owen ", "donald ", "dave ", "nate ", "mychael ", "bob ", "carter ", "harry ", "henry ", "gabriel ", "joseph ", "lucas ", "kent ", "brendan ", "kristopher ", "oscar ", "tony ", "tom ", "thomas ", "todd ","christian ", "lewis ", "nathan ", "brian ", "joseph ", "hiram ", "louis ", "d.b. weiss", "garth ", "howard ", "ernest ", "curtis ", "ed ", "gene ", "jemaine ", "don ", "matt ", "kurt ", "seth ", "barry ", "vince ", "alf ", "carl ", "russ ", "ryan ", "tree ", "martin ", "keegan ", "phil ", "kevin", "rich ", "jimmy ", "wayne ", "sean ", "dylan ", "mike ", "ross ", "tim ", "greg ", "gregg ", "steven ", "richard ", "chuck ", "doug ", "ricky ", "jack ", "james ", "rodrigo ", "alejandro ", "edward ", "ramin djawadi", "amin bhatia", "ari posner", "adrian ", "ken ", "ray ", "andrew ", "jamie ", "ronald ", "felix ", "w.g. snuffy walden", "william ", "harold ", "simon ", "trevor ", "bruce "]

# # Load the JSON file
# with open('male_staff_members.json', 'r') as f:
#     awards = json.load(f)

# # Iterate over the data and remove staff members whose names start with any name in the list
# for year, categories in list(awards.items()):
#     for category, staff_members in list(categories.items()):
#         for staff_member, details in list(staff_members.items()):
#             if any(staff_member.startswith(name) for name in names):
#                 del awards[year][category][staff_member]

# # Write the modified data back to the JSON file
# with open('tony_2.json', 'w') as f:
#     json.dump(awards, f, indent=4)


# import json

# # Load the data from the JSON file
# with open('oscar1_0.json', 'r') as f:
#     awards = json.load(f)

# # Initialize a dictionary to hold the short-named staff members
# short_named_staff = {}

# # Iterate over the data and add staff members with short names to the dictionary
# for year, categories in awards.items():
#     for category, staff_members in categories.items():
#         for staff_member, details in staff_members.items():
#             if len(staff_member) <= 7:
#                 if year not in short_named_staff:
#                     short_named_staff[year] = {}
#                 if category not in short_named_staff[year]:
#                     short_named_staff[year][category] = {}
#                 short_named_staff[year][category][staff_member] = details

# # Write the short-named staff members to a new JSON file
# with open('short_named.json', 'w') as f:
#     json.dump(short_named_staff, f, indent=4)


