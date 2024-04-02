from wonderwords import RandomWord
import os, time

while True:
    os.system("clear")
    r = RandomWord()
    word = r.word(word_min_length=6, word_max_length=6)
    print("welcome to wordle but with 6 letters instead of 5.")
    print("You have 7 guesses.")
    while True:
        guess = input("Enter your first guess\n> ")
        checkguess = w.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        