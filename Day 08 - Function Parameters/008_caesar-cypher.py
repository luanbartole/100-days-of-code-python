alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")


def caesar_cypher(base_text, shift_factor, function):
    encrypted_word = ""
    for letter in base_text:

        if function == "encode":
            if letter not in alphabet:
                encrypted_letter = letter
            elif alphabet.index(letter) + shift_factor <= len(alphabet) - 1:
                encrypted_letter = alphabet[alphabet.index(letter) + shift_factor]
            else:
                encrypted_letter = alphabet[alphabet.index(letter) + shift_factor - len(alphabet)]
            encrypted_word += encrypted_letter
        if function == "decode":
            if letter not in alphabet:
                decrypted_letter = letter
            elif alphabet.index(letter) + shift_factor >= 0:
                decrypted_letter = alphabet[alphabet.index(letter) - shift_factor]
            else:
                decrypted_letter = len(alphabet) - alphabet[alphabet.index(letter) + shift_factor]
            encrypted_word += decrypted_letter
    print(encrypted_word)


end_program = False
while not end_program:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cypher(text, shift, direction)
    if input("\nWould you like to do another cypher? [Y] or [N]:\n").upper() == "N":
        end_program = True
