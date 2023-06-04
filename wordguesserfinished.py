secret_word = "baseball"
guessed_letters = []
incorrect_letters = []
max_attempts = 15
attempts = 0

print("Welcome to the Word Guessing Game! You have 15 guesses and correct guesses do not count towards your attempts."
      " Good luck!")

while True:
    letter = input("Enter a letter: ")

    if letter in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(letter)

    if letter in secret_word:
        print("Correct guess!")
    else:
        print("Incorrect guess.")
        attempts += 1
        incorrect_letters.append(letter)
        incorrect_string = str(incorrect_letters)
        print("Incorrect letters: " + incorrect_string)

    revealed_word = ""
    for char in secret_word:
        if char in guessed_letters:
            revealed_word += char
        else:
            revealed_word += "_"

    print("Word:", revealed_word)
    print("Attempts:", attempts)

    if revealed_word == secret_word:
        print("Congratulations! You guessed the word correctly!")
        break

    if attempts == max_attempts:
        print("Maximum number of attempts reached, better luck next time!")
        break