import os, time
from colorama import Fore, Back, Style
import wonderwords
from wonderwords import RandomWord

while True:
    os.system("clear")
    firstguess = False
    secondguess = False
    thirdguess = False
    fourthguess = False
    fifthguess = False
    sixthguess = False
    Seventhguess = False
    r = RandomWord()
    word = r.word(word_min_length=6, word_max_length=6)
    print("welcome to wordle but with 6 letters instead of 5.")
    print("You have 7 guesses.")
    while not firstguess:
        guess = input(Fore.WHITE + "Enter your first guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] in word[1:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] not in word[0:6]:
            print(Fore.WHITE + guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == word[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] in word[0:1] + word[2:6]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] not in word[0:6]:
            print(Fore.WHITE + guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == word[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] in word[0:2] + word[3:6]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] not in word[0:6]:
            print(Fore.WHITE + guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == word[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] in word[0:3] + word[4:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] not in word[0:6]:
            print(Fore.WHITE + guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == word[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] in word[0:4] + word[5:6]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] not in word[0:6]:
            print(Fore.WHITE + guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == word[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            firstguess = True
        elif guess[5] == word[0:5]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            firstguess = True
        elif guess[5] not in word[0:6]:
            print(Fore.WHITE + guess[5] + " Wrong letter, Wrong spot")
            firstguess = True
    while not secondguess:
        guess = input(Fore.WHITE + "Enter your second guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] in word[1:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] not in word[0:6]:
            print(Fore.WHITE + guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == word[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] in word[0:1] + word[2:6]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] not in word[0:6]:
            print(Fore.WHITE + guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == word[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] in word[0:2] + word[3:6]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] not in word[0:6]:
            print(Fore.WHITE + guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == word[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] in word[0:3] + word[4:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] not in word[0:6]:
            print(Fore.WHITE + guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == word[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] in word[0:4] + word[5:6]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] not in word[0:6]:
            print(Fore.WHITE + guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == word[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            secondguess = True
        elif guess[5] in word[0:5]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            secondguess = True
        elif guess[5] not in word[0:6]:
            print(Fore.WHITE + guess[5] + " Wrong letter, Wrong spot")
            secondguess = True
    while not thirdguess:
        guess = input(Fore.WHITE + "Enter your third guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] in word[1:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] not in word[0:6]:
            print(Fore.WHITE + guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == word[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] in word[0:1] + word[2:6]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] not in word[0:6]:
            print(Fore.WHITE + guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == word[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] in word[0:2] + word[3:6]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] not in word[0:6]:
            print(Fore.WHITE + guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == word[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] in word[0:3] + word[4:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] not in word[0:6]:
            print(Fore.WHITE + guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == word[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] in word[0:4] + word[5:6]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] not in word[0:6]:
            print(Fore.WHITE + guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == word[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            thirdguess = True
        elif guess[5] in word[0:5]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            thirdguess = True
        elif guess[5] not in word[0:6]:
            print(Fore.WHITE + guess[5] + " Wrong letter, Wrong spot")
            thirdguess = True
    while not fourthguess:
        guess = input(Fore.WHITE + "Enter your fourth guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] in word[1:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] not in word[0:6]:
            print(Fore.WHITE + guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == word[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] in word[0:1] + word[2:6]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] not in word[0:6]:
            print(Fore.WHITE + guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == word[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] in word[0:2] + word[3:6]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] not in word[0:6]:
            print(Fore.WHITE + guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == word[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] in word[0:3] + word[4:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] not in word[0:6]:
            print(Fore.WHITE + guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == word[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] in word[0:4] + word[5:6]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] not in word[0:6]:
            print(Fore.WHITE + guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == word[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            fourthguess = True
        elif guess[5] in word[0:5]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            fourthguess = True
        elif guess[5] not in word[0:6]:
            print(Fore.WHITE + guess[5] + " Wrong letter, Wrong spot")
            fourthguess = True
    while not fifthguess:
        guess = input(Fore.WHITE + "Enter your fifth guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] in word[1:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] not in word[0:6]:
            print(Fore.WHITE + guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == word[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] in word[0:1] + word[2:6]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] not in word[0:6]:
            print(Fore.WHITE + guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == word[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] in word[0:2] + word[3:6]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] not in word[0:6]:
            print(Fore.WHITE + guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == word[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] in word[0:3] + word[4:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] not in word[0:6]:
            print(Fore.WHITE + guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == word[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] in word[0:4] + word[5:6]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] not in word[0:6]:
            print(Fore.WHITE + guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == word[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            fifthguess = True
        elif guess[5] in word[0:5]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            fifthguess = True
        elif guess[5] not in word[0:6]:
            print(Fore.WHITE + guess[5] + " Wrong letter, Wrong spot")
            fifthguess = True
    while not sixthguess:
        guess = input(Fore.WHITE + "Enter your sixth guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] in word[1:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] not in word[0:6]:
            print(Fore.WHITE + guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == word[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] in word[0:1] + word[2:6]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] not in word[0:6]:
            print(Fore.WHITE + guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == word[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] in word[0:2] + word[3:6]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] not in word[0:6]:
            print(Fore.WHITE + guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == word[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] in word[0:3] + word[4:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] not in word[0:6]:
            print(Fore.WHITE + guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == word[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] in word[0:4] + word[5:6]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] not in word[0:6]:
            print(Fore.WHITE + guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == word[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            sixthguess = True
        elif guess[5] in word[0:5]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            sixthguess = True
        elif guess[5] not in word[0:6]:
            print(Fore.WHITE + guess[5] + " Wrong letter, Wrong spot")
            sixthguess = True
    while not seventhguess:
        guess = input(Fore.WHITE + "Enter your seventh guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            print("That's not a valid guess, try again")
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            print(Fore.GREEN + guess[0] + " Right letter, Right spot")
        elif guess[0] in word[1:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[0] not in word[0:6]:
            print(Fore.WHITE + guess[0] + " Wrong letter, Wrong spot")
        if guess[1] == word[1]:
            print(Fore.GREEN + guess[1] + " Right letter, Right spot")
        elif guess[1] in word[0:1] + word[2:6]:
            print(Fore.YELLOW + guess[1] + " Right letter, Wrong spot")
        elif guess[1] not in word[0:6]:
            print(Fore.WHITE + guess[1] + " Wrong letter, Wrong spot")
        if guess[2] == word[2]:
            print(Fore.GREEN + guess[2] + " Right letter, Right spot")
        elif guess[2] in word[0:2] + word[3:6]:
            print(Fore.YELLOW + guess[2] + " Right letter, Wrong spot")
        elif guess[2] not in word[0:6]:
            print(Fore.WHITE + guess[2] + " Wrong letter, Wrong spot")
        if guess[3] == word[3]:
            print(Fore.GREEN + guess[3] + " Right letter, Right spot")
        elif guess[3] in word[0:3] + word[4:6]:
            print(Fore.YELLOW + guess[0] + " Right letter, Wrong spot")
        elif guess[3] not in word[0:6]:
            print(Fore.WHITE + guess[3] + " Wrong letter, Wrong spot")
        if guess[4] == word[4]:
            print(Fore.GREEN + guess[4] + " Right letter, Right spot")
        elif guess[4] in word[0:4] + word[5:6]:
            print(Fore.YELLOW + guess[4] + " Right letter, Wrong spot")
        elif guess[4] not in word[0:6]:
            print(Fore.WHITE + guess[4] + " Wrong letter, Wrong spot")
        if guess[5] == word[5]:
            print(Fore.GREEN + guess[5] + " Right letter, Right spot")
            seventhguess = True
        elif guess[5] in word[0:5]:
            print(Fore.YELLOW + guess[5] + " Right letter, Wrong spot")
            seventhguess = True
        elif guess[5] not in word[0:6]:
            print(Fore.WHITE + guess[5] + " Wrong letter, Wrong spot")
            seventhguess = True
    print("You lost, the game will reset in 3 seconds")
    time.sleep(3)
    
