import random
import art


def color_line(line, color):
    """Used for coloring the terminal lines."""
    if color == "red":
        return "\033[91m{}\033[00m".format(line)
    if color == "green":
        return "\033[92m{}\033[00m".format(line)
    if color == "blue":
        return "\033[94m{}\033[00m".format(line)


def guess(lives, answer):
    """Input and compare player's guess to the computer's number for appropriate response"""
    # Loop for the player to guess until he loses all of his lives.
    while lives != 0:
        print()
        player_guess = int(input("Guess a number between 1 and 100: "))
        # Compare the player guess to the random number generated
        if player_guess == answer:
            print(color_line(f"You won! The correct number was {player_guess}", "green"))

            break
        else:

            # Gives the player a hint if it's too high or too low if he has more lives.
            if player_guess > answer:
                print(color_line("Too high!", "blue"))
            if player_guess < answer:
                print(color_line("Too low!", "blue"))
            # End of game message if the player lost all of his lives.
            if lives == 1:
                print(color_line("Game over!", "red"))
        lives -= 1


def guess_the_number_game(game_mode):
    """Runs the whole game of Guess The Number on the given game mode"""
    # Generate the computer's number.
    computer_number = random.randrange(1, 101)
    # Let the player guess based on the game mode. the easy level gives the user 10 lives and the hard one 5 lives.
    if game_mode == "Easy":
        guess(10, computer_number)
    if game_mode == "Hard":
        guess(5, computer_number)


# Prints the logo of the game.
print("-" * 90)
print(art.logo)
print("-" * 90)

# Runs the game while the user decides to keep playing.
while input("\nStart a new game? [Y] or [N]: ").upper() != "N":
    difficulty_level = input("Choose a difficulty level: [Easy] or [Hard]: ").capitalize()
    guess_the_number_game(difficulty_level)
    print("-" * 90)
