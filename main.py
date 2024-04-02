import enchant
import wonderwords
from wonderwords import RandomWord
import os, time

while True:
    os.system("clear")
    x = 
    r = RandomWord()
    word = r.word(word_min_length=6, word_max_length=6)
    print("welcome to wordle but with 6 letters instead of 5.")
    print("You have 7 guesses.")
    while not x:
        guess = input("Enter your first guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess[0] == r[0]:
            print(guess[0] + "Right letter, Right spot")
        elif guess[0] == r[1,2,3,4,5]:
            print(guess[0] + "Right letter, Wrong spot")
        elif guess[0] != r[0,1,2,3,4,5]:
            
