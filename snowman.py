"""Melting Snowman game - a word guessing game."""
import random

# ASCII art representing the snowman melting stages
SNOWMAN_STAGES = [
    """
       _===_
      (., .)
      ( : )
     ( : : )
    """,  # 0 mistakes
    """
      (., .)
      ( : )
     ( : : )
    """,  # 1 mistake
    """
      (.. )
      ( : )
     ( : : )
    """,  # 2 mistakes
    """
     ( : : )
    """,  # 3 mistakes
    """
     _______ (Just a puddle of water!)
    """  # 4 mistakes (Game Over)
]

WORD_LIST = ["python", "program", "developer", "snowman", "computer", "algorithm"]


def choose_word():
    """Pick a random word from the word list."""
    return random.choice(WORD_LIST)


def display_word(word, guessed_letters):
    """Return the hidden word string with underscores for unguessed letters."""
    displayed = []
    for letter in word:
        if letter in guessed_letters:
            displayed.append(letter)
        else:
            displayed.append("_")
    return " ".join(displayed)


def main():
    print("Welcome to Melting Snowman!")

    secret_word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    # Maximum mistakes is based on the number of snowman stages minus 1
    max_mistakes = len(SNOWMAN_STAGES) - 1

    # Main game loop
    while wrong_guesses < max_mistakes:
        print(SNOWMAN_STAGES[wrong_guesses])
        print(f"Word to guess: {display_word(secret_word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Get user input and ensure it's a valid single letter
        guess = input("Guess a letter: ").strip().lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'!")
            continue

        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Check for win condition
            if "_" not in display_word(secret_word, guessed_letters):
                print(f"\nCongratulations! You saved the snowman! The word was: {secret_word}")
                break
        else:
            print(f"Oops! '{guess}' is not in the word.")
            wrong_guesses += 1

    # Game over condition
    if wrong_guesses == max_mistakes:
        print(SNOWMAN_STAGES[wrong_guesses])
        print(f"Game Over! The snowman has melted completely. The word was: {secret_word}")


if __name__ == "__main__":
    main()

