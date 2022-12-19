# This program lets you customize a character and then uses the variables to start an introduction to a text-based adventure story.
print("---Character Builder---")
name = input("Choose your name: ")
race = input("Choose your race (orc, human, elf etc.): ")
color = input("Choose a color: ")
print("-"*21)
print("Welcome", name + "! You are now a official soldier of the", color,
      "guild. Do your best to make the", race, "race proud of you!")
print("-"*21)
