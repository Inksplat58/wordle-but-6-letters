import os, time
from colorama import Fore, Back, Style
import wonderwords
from wonderwords import RandomWord

while True:
    os.system("clear")
    x = False
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
        if guess == r:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == r[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] == r[1,2,3,4,5]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] != r[0,1,2,3,4,5]:
            print(guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == r[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] == r[0,2,3,4,5]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] != r[0,1,2,3,4,5]:
            print(guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == r[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] == r[0,1,3,4,5]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] != r[0,1,2,3,4,5]:
            print(guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == r[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] == r[0,1,2,4,5]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] != r[0,1,2,3,4,5]:
            print(guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == r[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] == r[0,1,2,3,5]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] != r[0,1,2,3,4,5]:
            print(guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == r[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            x = True
        elif guess[5] == r[0,1,2,3,4]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            x = True
        elif guess[5] != r[0,1,2,3,4,5]:
            print(guess[5] + " Wrong letter, Wrong spot")
            x = True
    
        
