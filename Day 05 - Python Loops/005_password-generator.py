import random

# Lists that will be used to generate a password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Start of the program and header / input
print("-" * 20 + "\nPassword Generator\n" + "-" * 20 + "\nHow many do you want of each of this:")
user_letters = int(input("Letters: "))
user_symbols = int(input(f"Symbols: "))
user_numbers = int(input(f"Numbers: "))

# Set the list that will be used to generate the password
password_base = []

# Assign random values on the password_base list based on what the user input previously.
for x in range(0, user_letters):
    password_base.append(random.choice(letters))
for x in range(0, user_symbols):
    password_base += random.choice(symbols)
for x in range(0, user_numbers):
    password_base += random.choice(numbers)

# Shuffle the items on the list changing its positions and join the list into a string.
random.shuffle(password_base)
final_pass = "".join(password_base)
print(f"\nFinal Password: {final_pass}")
