import art

# Dictionary of resources the coffee machine has.
resources = {
    "water": 300,
    "coffee": 200,
    "milk": 100,
    "money": 0
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# Dictionary of recipes and cost of each beverage.
menu = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    }
}


def enough_resources(drink):
    """Check if the machine has enough resources to do the beverage selected"""
    # For each ingredient in the drink recipe, check if the machine have enough of it to make it.
    low_resources = []  # List of resources the machine doesn't have to make the beverage.
    for item in menu[drink]["ingredients"]:
        if resources[item] < menu[drink]["ingredients"][item]:
            # If it doesn't have the resource, it adds it to the list of low resources.
            low_resources.append(item)
    if low_resources:
        print("Sorry! I don't have enough " + " / ".join(low_resources) + " to make your order.\n")
        return True


def order_drink():
    """Calls the correspondent step of the assembly line in order to make the coffee"""
    available_command = False  # Variable used to return that the user used an available command when he does.

    # Keep looping through a step while the user does not put an available command so the code doesn't break.
    while not available_command:
        available_command = True
        # Display the list of drinks the user can choose from.
        print("=" * 30 + "Menu" + "=" * 30 + "\n[1] Expresso \n[2] Latte \n[3] Cappuccino\n" + "=" * 64)
        # Prompt the user to select a beverage and decides how to act based on it.
        choose = input("Choose your drink: ").capitalize()
        print()
        match choose:
            # Check if the machine has enough resources to make the drink.
            case "1":
                drink = "expresso"
                cannot_make_the_drink = enough_resources("expresso")
                if cannot_make_the_drink:
                    available_command = False
                else:
                    return drink
            case "2":
                drink = "latte"
                cannot_make_the_drink = enough_resources("latte")
                if cannot_make_the_drink:
                    available_command = False
                else:
                    return drink
            case "3":
                drink = "cappuccino"
                cannot_make_the_drink = enough_resources("cappuccino")
                if cannot_make_the_drink:
                    available_command = False
                else:
                    return drink
            # Turn the coffee machine off (ends the program)
            case "Off":
                exit()
            # Displays a report of the resources left in the coffee machine.
            case "Report":
                print("-" * 5 + "Resources" + "-" * 5)
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print(f"Money: ${resources['money']}")
                print("")
                available_command = False
            # If the player types an unknown command, it sets the loop to restart with the available_command variable.
            case other:
                print("Command not found, let's try again!\n")
                available_command = False
        # Step #2 - Processing the coins


def coin_processor(drink):
    print()
    client_money = 0 # Money the client has put into the machine.
    cost_of_drink = menu[drink]['cost']
    print(f"Insert Coins [${cost_of_drink}]:")
    # Scans the coins dictionary to ask the user how manny pennies, nickles, dimes and quarters he'll use to pay.
    for item in coins:
        client_money += float(input(f"{item.capitalize()}: ")) * coins[item]
    print(f"\nTotal Money: ${round(client_money, 2)}")
    print(f"Cost of {drink}: ${cost_of_drink}")
    # Checks if the value is low, right or too much and refund or give change to the client.
    if client_money < cost_of_drink:
        print("\nSorry! Not enough money. Coins refunded.")
    elif client_money == cost_of_drink:
        resources['money'] += cost_of_drink
        print("\nThe transaction was a success!")
        return "Success"
    elif client_money > cost_of_drink:
        resources['money'] += cost_of_drink
        change = client_money - cost_of_drink
        print(f"Your change is ${round(change, 2)}")
        print("\nThe transaction was a success!")
        return "Success"


def make_coffee(drink):
    # Deduct the resources based on the ingredients used to make the beverage.
    for item in menu[drink]["ingredients"]:
        resources[item] -= menu[drink]["ingredients"][item]
    print(f"\n{art.cup_of_coffee}")


def coffee_machine():
    # Repeats the process until user asks to stop the program.
    repeat = True
    while repeat:
        print(art.logo)
        # Order the drink
        order = order_drink()
        # Deals with the transaction money
        payment = coin_processor(order)
        if payment == "Success":
            # Make the coffee the client ordered
            make_coffee(order)
        if input("Would you like to order again? [Y] or [N]: ").capitalize() == "N":
            repeat = False


coffee_machine()
