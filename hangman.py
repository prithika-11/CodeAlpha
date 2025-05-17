import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    word = random.choice(words)
    guessed_letters = []
    tries = 6  # Number of allowed incorrect guesses

    print("Welcome to Hangman!")
    
    while tries > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word:", display_word)

        if display_word == word:
            print("Congratulations! You've guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            tries -= 1
            print(f"Wrong guess. You have {tries} tries left.")

    else:
        print(f"Game over. The word was '{word}'.")

hangman()
