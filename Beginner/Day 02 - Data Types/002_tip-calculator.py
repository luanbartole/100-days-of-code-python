# This program calculates the split bill based on the tip percentage and people paying for it.

# Prints the header
print("-"*15+"\nTip Calculator\n"+"-"*15)

# Input the variables it needs
bill = float(input("Total bill: $"))
# Input and calculate the tip total based on the bill and percentage of the tip typed.
tip = bill/100*float(input("Tip percentage: "))
people = int(input("People paying the bill: "))

# Print the calculus of how the bill should be split, rounded to two decimal numbers.
# First it calculates the final bill including the tip, then it divides it by the number of people paying.
# Finally, it prints out the footer.
print(f"\nBill for each person: ${round((bill+tip)/people,2)}\n"+"-"*15)
