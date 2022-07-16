from art import logo


def Sum(n1, n2):
    return n1 + n2


def Subtraction(n1, n2):
    return n1 - n2


def Multiplication(n1, n2):
    return n1 * n2


def Division(n1, n2):
    return n1 / n2


calculator = {
    "+": Sum,
    "-": Subtraction,
    "*": Multiplication,
    "/": Division
}

end_program = False
num1 = 0

while not end_program:
    print(logo)

    print("-" * 104)
    if num1 == 0:
        num1 = float(input("\n1º Number: "))
    op_symbol = input("\nOperation (+, -, * or /): ")
    num2 = float(input("\n2º Number: "))
    op_function = calculator[op_symbol]
    num3 = op_function(num1, num2)

    print(f"\n{num1} {op_symbol} {num2} = {num3}\n")
    choice1 = input("Perform another operation using this result? [Y] or [N]: ").capitalize()
    if choice1 == "Y":
        num1 = num3
    else:
        choice2 = input("Keep doing operations? [Y] or [N]: ").capitalize()
        if choice2 == "Y":
            num1 = 0
        else:
            end_program = True

print("-" * 104)
print("See ya later!")
print("-" * 104)
