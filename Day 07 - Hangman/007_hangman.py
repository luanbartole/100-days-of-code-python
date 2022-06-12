import random
import hangman_words
import hangman_art

# Sets the list of possible words, the chosen word, lives and creates an empty list for the user guesses
chosen_word = random.choice(hangman_words.word_list)
display = []
user_guesses = []
lives = 6
for char in chosen_word:
    display.append("_")

# Print header and chosen word blank (display)
print("=" * 50 + f"\n{hangman_art.logo}\n\n" + "=" * 50)
print("\nWord:", "".join(display))

# User guesses letters until he wins the game
while "".join(display) != chosen_word and lives != 0:
    # Asks the user's letter guess and adds the guess into a list with all player guesses
    guess = input("Choose a letter: ").lower()

    # Takes a life away if the guess is wrong, and it is the first time guessing that letter.
    # Tells the player if he has already guessed the letter.
    if guess not in user_guesses:
        user_guesses.append(guess)
        if guess not in chosen_word:
            print(f"\nThe letter '{guess.upper()}' is not in the chosen word.\nTry another letter.")
            lives -= 1
    else:
        if guess not in chosen_word:
            print(
                f"\nThe letter '{guess.upper()}' is not in the chosen word and you already guessed it.\nTry another letter.")
        else:
            print(f"\nYou have already guessed the letter '{guess.upper()}'. Try another letter.")

    # Substitute a blank space for its corresponding character if the guess is right
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    # Output the current stage and display
    print(f"{hangman_art.stages[lives]} \nWord: {''.join(display)}")
# The loop ends and the player wins or lose the game
print("\n" + "=" * 30)
print("You Won! Congratulations") if lives != 0 else print(f"You Lost!\nThe chosen word was {chosen_word.capitalize()}")
print("=" * 30)
