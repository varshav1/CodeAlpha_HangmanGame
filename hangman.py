import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect attempts allowed
attempts = 6

# Display hidden word
display = ["_"] * len(word)

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts remaining:", attempts)

    guess = input("Guess a letter: ").lower()

    # Check whether input is a single alphabet
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        attempts -= 1
        print("Wrong guess!")

# Game result
if "_" not in display:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)