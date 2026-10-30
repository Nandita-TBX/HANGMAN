import random
from Words import hangman_words
import string
def valid():
    word = random.choice(hangman_words)
    return word.upper()
def hangman():
    word = valid()
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used = set()
    lives = 10
    while len(letters) > 0 and lives > 0:
        print("You have", lives, "lives  left and you have used the letters: "," ".join(used))
        word_list = [letter if letter in used else "-" for letter in word]
        print("Current word: "," ".join(word_list))
        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet - used:
            used.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
                print(" ")
            else:
                lives -= 1
                print("Your letter", user_letter, "is not in the word.")
        elif user_letter in used:
            print("You have already guessed that letter. Please guess a new one instead.")
        else:
            print("Invalid letter.")
    if lives == 0:
        print("You have died. The word was", word)
    else:
        print("Congratulations! You guessed", word, "!")
hangman()