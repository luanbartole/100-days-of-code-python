# Open csv containing the data.
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# List comprehension of the nato alphabet based on each letter of the name.
name = input("Write a name: ").upper()
nato_name = [phonetic_dict[letter] for letter in name]
print(nato_name)
