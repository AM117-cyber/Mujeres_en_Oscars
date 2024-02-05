# Open the file in read mode and get the names
with open('male_emmys.txt', 'r') as f:
    names = f.readlines()

# Filter out names that start with 'David', 'Sam', or 'Joe'
names = [name for name in names if not (name.startswith('rick ') or name.startswith('joss ') or name.startswith('mitchell ') or name.startswith('aaron ') or name.startswith('christopher ') or name.startswith('paul ') or name.startswith('joe '))]

# Open the file in write mode and write the remaining names
with open('emmys_1.txt', 'w') as f:
    f.writelines(names)
