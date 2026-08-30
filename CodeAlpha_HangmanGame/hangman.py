import random

# List of predefined words
words = ["python", "coding", "laptop", "planet", "coffee"]

# Randomly select a word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("=" * 35)
print("         HANGMAN GAME")
print("=" * 35)

while incorrect_guesses < max_incorrect_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print(f"Incorrect Guesses: {incorrect_guesses}/{max_incorrect_guesses}")

    # Check whether the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You have already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)