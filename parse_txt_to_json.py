import json

def add_gender_property(input_file, women_file, output_file):
    # Load the data from the input file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Load the data from the women file
    with open(women_file, 'r') as f:
        women_data = json.load(f)
    
    # Get a set of all female staff member names
    women = set()
    for year, categories in women_data.items():
        for category, staff_members in categories.items():
            for staff_member in staff_members.keys():
                women.add(staff_member)
    
    # Add the 'gender' property to each staff member in the input data
    for year, categories in data.items():
        for category, staff_members in categories.items():
            for staff_member in staff_members.keys():
                if staff_member in women:
                    data[year][category][staff_member]['gender'] = 'female'
                else:
                    data[year][category][staff_member]['gender'] = 'male'
    
    # Write the modified data to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Call the function
add_gender_property('emmys_complete.json', 'emmys_women.json', 'emmys_complete.json')

# import json
# from collections import OrderedDict

# def merge_json_files(file1, file2, output_file):
#     # Load the data from the first file
#     with open(file1, 'r') as f:
#         data1 = json.load(f)
    
#     # Load the data from the second file
#     with open(file2, 'r') as f:
#         data2 = json.load(f)
    
#     # Merge the data
#     merged_data = {**data1, **data2}
    
#     # Sort the data by year
#     sorted_data = OrderedDict(sorted(merged_data.items()))
    
#     # Write the sorted data to the output file
#     with open(output_file, 'w') as f:
#         json.dump(sorted_data, f, indent=4)

# # Call the function
# merge_json_files('emmys.json', 'emmys_extra.json', 'emmys_complete.json')


# import csv
# import json

# def parse_csv_to_json(filename):
#     # Define the mapping from categories to sets
#     category_mapping = {
#         'directing': [
#             'Outstanding Directing For A Limited Or Anthology Series Or Movie',
#             'Outstanding Directing For A Variety Special',
#             'Outstanding Directing For A Drama Series',
#             'Outstanding Directing For A Variety Series',
#             'Outstanding Directing For A Limited Series, Movie Or Dramatic Special',
#             'Outstanding Directing For A Documentary/Nonfiction Program',
#             'Outstanding Directing For A Comedy Series',
#             'Outstanding Directing For A Reality Program'
#         ],
#         'music': [
#             'Outstanding Music Supervision',
#             'Outstanding Music Composition For A Series (Original Dramatic Score)',
#             'Outstanding Original Music And Lyrics',
#             'Outstanding Music Composition For A Limited Or Anthology Series, Movie Or Special (Original Dramatic Score)',
#             'Outstanding Music Composition For A Limited Series, Movie Or Special (Original Dramatic Score)',
#             'Outstanding Music Direction',
#             'Outstanding Music Composition For A Documentary Series Or Special (Original Dramatic Score)',
#             'Outstanding Original Main Title Theme Music'
#         ],
#         'writing': [
#             'Outstanding Writing For A Comedy Series',
#             'Outstanding Writing For A Limited Series, Movie Or Dramatic Special',
#             'Outstanding Writing For A Limited Or Anthology Series Or Movie',
#             'Outstanding Writing For A Drama Series',
#             'Outstanding Writing For A Variety Series',
#             'Outstanding Writing For A Variety Special'
#         ]
#     }
#     # Flatten the mapping to a dictionary for easy lookup
#     category_lookup = {category.lower(): key for key, categories in category_mapping.items() for category in categories}

#     data = {}
#     with open(filename, 'r') as f:
#         reader = csv.reader(f)
#         next(reader)  # Skip the header
#         for row in reader:
#             year, category, staff, name_of_work, winner = row
#             category = category_lookup.get(category.lower(), category)  # Map the category to its set
#             for staff_member in staff.split(', '):  # Split the staff members
#                 if year not in data:
#                     data[year] = {}
#                 if category not in data[year]:
#                     data[year][category] = {}

#                 data[year][category][staff_member.lower()]= {
#                     'name_of_work': name_of_work.lower(),
#                     'winner': winner.lower() == 'true'
#                 }

#     with open('emmys_extra.json', 'w') as f:
#         json.dump(data, f, indent=4)

# # Call the function
# parse_csv_to_json('emmys_extra.csv')



# import csv

# def parse_txt_to_csv(filename):
#     data = []
#     with open(filename, 'r') as f:
#         lines = [line.strip() for line in f.readlines() if line.strip()]
        
#     i = 0
#     while i < len(lines):
#         if ' - ' in lines[i] and lines[i].startswith('Outstanding'):
#             category, year = lines[i].split(' - ')
#             i += 1
#             staff_members = []
#             # Now we keep reading staff members until we hit a line that's either 'NOMINEE' or 'WINNER'
#             while lines[i] not in ['NOMINEE', 'WINNER']:
#                 staff_member, _ = lines[i].split(', ')
#                 print(staff_member)
#                 staff_members.append(staff_member)
#                 i += 1
#             winner = lines[i] == 'WINNER'
#             i += 1
#             name_of_work = lines[i]
#             i += 1  # Move to the next line
#             # Now we skip lines until we hit the next category or run out of lines
#             while i < len(lines) and not (lines[i].startswith('Outstanding') and ' - ' in lines[i]):
#                 i += 1
#             data.append([year, category, ', '.join(staff_members), name_of_work, winner])
#         else:
#             i += 1
    
#     with open('emmys_extra.csv', 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['year', 'category', 'staff', 'name_of_work', 'winner'])
#         writer.writerows(data)

# # Call the function
# #parse_txt_to_csv('test.txt')
# parse_txt_to_csv('new_emmys_extra_years.txt')

# import csv

# def write_unique_categories_to_txt(csv_filename, txt_filename):
#     categories = set()
#     with open(csv_filename, 'r') as f:
#         reader = csv.reader(f)
#         next(reader)  # Skip the header
#         for row in reader:
#             categories.add(row[1])  # The category is in the second column
    
#     with open(txt_filename, 'w') as f:
#         for category in categories:
#             f.write(category + '\n')

# # Call the function
# write_unique_categories_to_txt('emmys_extra.csv', 'categ.txt')
