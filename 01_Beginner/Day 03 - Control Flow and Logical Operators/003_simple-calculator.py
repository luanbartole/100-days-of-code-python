# Printing the header
print("-" * 20 + "\nSimple Calculator\n" + "-" * 20)
print("[0] Sum\n[1] Subtraction\n[2] Division\n[3] Multiplication\n" + "-" * 20)

# This is where the user input the data
action = float(input("Select a action (number): "))

# Control flow that decides what math operation will be done.
# It can also stop the program if the user inputs any other number.
if action < 0 or action > 3:
    print("\nYou didn't select a available operation, do better next time.")
else:
    n1 = float(input("Number 1: "))
    n2 = float(input("Number 2: "))
    res = 0
    if action == 0:
        res = n1 + n2
    elif action == 1:
        res = n1 - n2
    elif action == 2:
        res = n1 / n2
    elif action == 3:
        res = n1 * n2
    # Here it prints the result of the selected operation.
    print(f"Result: {round(res, 2)}")
    print("-" * 20 + "\nThank you for using me! \nHave a great day!\n" + "-" * 20)
