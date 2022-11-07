import blackjack_art
import random

# Defines the deck of cards which is used in the game and the variable used to end the game.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def color_line(line, color):
    """Used for coloring the terminal lines."""
    if color == "red":
        return "\033[91m{}\033[00m".format(line)
    if color == "green":
        return "\033[92m{}\033[00m".format(line)


def deal_card():
    """Assign a random card to a player's hand."""
    new_card = random.choice(cards)
    return new_card


def calculate_score(player_cards):
    """Based on a list of cards it returns the player's total score."""
    # Check if one of the players has a blackjack and returns 0 instead of the score to represent it.
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0

    # If a player has a blackjack and the sum of cards is greater than 21, it turns it into a 1 instead of 11.
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
    return sum(player_cards)


def compare(user_score, computer_score):
    """Compares the user's and computer's scores to determine the winner and loser."""
    if user_score > 21 and computer_score > 21:
        return color_line("You busted! Computer Wins!", "red")

    if user_score == computer_score:
        return color_line("Draw", "green")
    elif computer_score == 0:
        return color_line("Opponent has a Blackjack! Computer Wins!", "red")
    elif user_score == 0:
        return color_line("You have a Blackjack! User Wins!", "green")
    elif user_score > 21:
        return color_line("You busted! Computer Wins!", "red")
    elif computer_score > 21:
        return color_line("Computer busted! User Wins!", "green")
    elif user_score > computer_score:
        return color_line("User Wins!", "green")
    else:
        return color_line("Computer Wins!", "red")


def blackjack_game():
    # Play game
    # Defines the 2 initial cards of both players and reveals the user's and the computer's first card
    print()
    user_cards = []
    computer_cards = []
    game_over = False

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        # Calculates the score of the players in the current round
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Displays the cards of the players in the current round
        print(color_line("User Stats", "green"))
        print("Cards:", user_cards)
        print("Score:", sum(user_cards))
        print()
        print(color_line("Computer Stats", "red"))
        print("First Card:", computer_cards[1])
        print("Score: ?")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("\nWant to get another card? [Y] or [N]: ").upper()
            if user_deal == "N":
                game_over = True
            if user_deal == "Y":
                user_cards.append(deal_card())
        print("-" * 100)

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("[END OF THE GAME]")
    print(f"\nUser's final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print("-"*100)
    return ""


# Prints the logo and asks for an input to start a new game.
print(blackjack_art.logo)
print("Welcome to your personal blackjack casino!")
print("-" * 100)

# Runs the game while the user decides to keep playing
while input("Start a new game? [Y] or [N]: ").upper() != "N":
    blackjack_game()
