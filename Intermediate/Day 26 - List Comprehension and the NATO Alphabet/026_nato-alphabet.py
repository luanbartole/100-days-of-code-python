# Open csv containing the data.
with open("nato_phonetic_alphabet.csv") as nato_file:
    # Strips each line of the "\n" and separates key:value by ","
    data = [item.strip("\n") for item in nato_file.readlines()]
    data_dict = {item.split(",")[0]: item.split(",")[1] for item in data}

# List comprehension of the nato alphabet based on each letter of the name.
name = input("Write a name: ")
nato_name = [data_dict[letter.upper()] for letter in name]
print(nato_name)


