# Sets the list of names to write letters for.
with open("Input/Names/invited_names.txt") as custom:
    name_list = custom.readlines()
    # Clean the /n of every list item and leaves the name only. Ex: turns "Luan\n" into "Luan"
    for _ in range(len(name_list)-1):
        name_list[_] = name_list[_].strip("\n")

# Sets the custom_letter with the name on it.
with open("Input/Letters/starting_letter.txt") as letter_file:

    # Sets the lines in the file, and for each name of the list it generates a custom_letter document.
    template_letter = letter_file.readlines()

for name in name_list:
    # Replace the placeholder with a name of the list.
    custom_name = template_letter[0].replace("[name]", name)
    template_letter[0] = custom_name

    # Creates the custom_letter
    custom_letter = ""
    for line in template_letter:
        custom_letter += line
    with open(f"Output/ReadyToSend/{name}", "w") as new_letter:
        new_letter.write(custom_letter)

    # Replace the name of the list with the placeholder again
    custom_name = template_letter[0].replace(name, "[name]")
    template_letter[0] = custom_name
