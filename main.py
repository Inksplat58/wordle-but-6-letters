import os, time
from colorama import Fore
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
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            letter1 = (Fore.GREEN + guess[0])
        elif guess[0] in word[1:6]:
            letter1 = (Fore.YELLOW + guess[0])
        elif guess[0] not in word[0:6]:
            letter1 = (Fore.WHITE + guess[0])
        if guess[1] == word[1]:
            letter2 = (Fore.GREEN + guess[1])
        elif guess[1] in word[0:1] + word[2:6]:
            letter2 = (Fore.YELLOW + guess[1])
        elif guess[1] not in word[0:6]:
            letter2 = (Fore.WHITE + guess[1])
        if guess[2] == word[2]:
            letter3 = (Fore.GREEN + guess[2])
        elif guess[2] in word[0:2] + word[3:6]:
            letter3 = (Fore.YELLOW + guess[2])
        elif guess[2] not in word[0:6]:
            letter3 = (Fore.WHITE + guess[2])
        if guess[3] == word[3]:
            letter4 = (Fore.GREEN + guess[3])
        elif guess[3] in word[0:3] + word[4:6]:
            letter4 = (Fore.YELLOW + guess[0])
        elif guess[3] not in word[0:6]:
            letter4 = (Fore.WHITE + guess[3])
        if guess[4] == word[4]:
            letter5 = (Fore.GREEN + guess[4])
        elif guess[4] in word[0:4] + word[5:6]:
            letter5 = (Fore.YELLOW + guess[4])
        elif guess[4] not in word[0:6]:
            letter5 = (Fore.WHITE + guess[4])
        if guess[5] == word[5]:
            letter6 = (Fore.GREEN + guess[5])
            firstguess = True
        elif guess[5] == word[0:5]:
            letter6 = (Fore.YELLOW + guess[5])
            firstguess = True
        elif guess[5] not in word[0:6]:
            letter6 = (Fore.WHITE + guess[5])
            firstguess = True
    print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
    while not secondguess:
        guess = input(Fore.WHITE + "Enter your second guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            letter1 = (Fore.GREEN + guess[0])
        elif guess[0] in word[1:6]:
            letter1 = (Fore.YELLOW + guess[0])
        elif guess[0] not in word[0:6]:
            letter1 = (Fore.WHITE + guess[0])
        if guess[1] == word[1]:
            letter2 = (Fore.GREEN + guess[1])
        elif guess[1] in word[0:1] + word[2:6]:
            letter2 = (Fore.YELLOW + guess[1])
        elif guess[1] not in word[0:6]:
            letter2 = (Fore.WHITE + guess[1])
        if guess[2] == word[2]:
            letter3 = (Fore.GREEN + guess[2])
        elif guess[2] in word[0:2] + word[3:6]:
            letter3 = (Fore.YELLOW + guess[2])
        elif guess[2] not in word[0:6]:
            letter3 = (Fore.WHITE + guess[2])
        if guess[3] == word[3]:
            letter4 = (Fore.GREEN + guess[3])
        elif guess[3] in word[0:3] + word[4:6]:
            letter4 = (Fore.YELLOW + guess[0])
        elif guess[3] not in word[0:6]:
            letter4 = (Fore.WHITE + guess[3])
        if guess[4] == word[4]:
            letter5 = (Fore.GREEN + guess[4])
        elif guess[4] in word[0:4] + word[5:6]:
            letter5 = (Fore.YELLOW + guess[4])
        elif guess[4] not in word[0:6]:
            letter5 = (Fore.WHITE + guess[4])
        if guess[5] == word[5]:
            letter6 = (Fore.GREEN + guess[5])
            secondguess = True
        elif guess[5] == word[0:5]:
            letter6 = (Fore.YELLOW + guess[5])
            secondguess = True
        elif guess[5] not in word[0:6]:
            letter6 = (Fore.WHITE + guess[5])
            secondguess = True
    print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
    while not thirdguess:
        guess = input(Fore.WHITE + "Enter your third guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            letter1 = (Fore.GREEN + guess[0])
        elif guess[0] in word[1:6]:
            letter1 = (Fore.YELLOW + guess[0])
        elif guess[0] not in word[0:6]:
            letter1 = (Fore.WHITE + guess[0])
        if guess[1] == word[1]:
            letter2 = (Fore.GREEN + guess[1])
        elif guess[1] in word[0:1] + word[2:6]:
            letter2 = (Fore.YELLOW + guess[1])
        elif guess[1] not in word[0:6]:
            letter2 = (Fore.WHITE + guess[1])
        if guess[2] == word[2]:
            letter3 = (Fore.GREEN + guess[2])
        elif guess[2] in word[0:2] + word[3:6]:
            letter3 = (Fore.YELLOW + guess[2])
        elif guess[2] not in word[0:6]:
            letter3 = (Fore.WHITE + guess[2])
        if guess[3] == word[3]:
            letter4 = (Fore.GREEN + guess[3])
        elif guess[3] in word[0:3] + word[4:6]:
            letter4 = (Fore.YELLOW + guess[0])
        elif guess[3] not in word[0:6]:
            letter4 = (Fore.WHITE + guess[3])
        if guess[4] == word[4]:
            letter5 = (Fore.GREEN + guess[4])
        elif guess[4] in word[0:4] + word[5:6]:
            letter5 = (Fore.YELLOW + guess[4])
        elif guess[4] not in word[0:6]:
            letter5 = (Fore.WHITE + guess[4])
        if guess[5] == word[5]:
            letter6 = (Fore.GREEN + guess[5])
            thirdguess = True
        elif guess[5] == word[0:5]:
            letter6 = (Fore.YELLOW + guess[5])
            thirdguess = True
        elif guess[5] not in word[0:6]:
            letter6 = (Fore.WHITE + guess[5])
            thirdguess = True
    print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
    while not fourthguess:
        guess = input(Fore.WHITE + "Enter your fourth guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:           
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            letter1 = (Fore.GREEN + guess[0])
        elif guess[0] in word[1:6]:
            letter1 = (Fore.YELLOW + guess[0])
        elif guess[0] not in word[0:6]:
            letter1 = (Fore.WHITE + guess[0])
        if guess[1] == word[1]:
            letter2 = (Fore.GREEN + guess[1])
        elif guess[1] in word[0:1] + word[2:6]:
            letter2 = (Fore.YELLOW + guess[1])
        elif guess[1] not in word[0:6]:
            letter2 = (Fore.WHITE + guess[1])
        if guess[2] == word[2]:
            letter3 = (Fore.GREEN + guess[2])
        elif guess[2] in word[0:2] + word[3:6]:
            letter3 = (Fore.YELLOW + guess[2])
        elif guess[2] not in word[0:6]:
            letter3 = (Fore.WHITE + guess[2])
        if guess[3] == word[3]:
            letter4 = (Fore.GREEN + guess[3])
        elif guess[3] in word[0:3] + word[4:6]:
            letter4 = (Fore.YELLOW + guess[0])
        elif guess[3] not in word[0:6]:
            letter4 = (Fore.WHITE + guess[3])
        if guess[4] == word[4]:
            letter5 = (Fore.GREEN + guess[4])
        elif guess[4] in word[0:4] + word[5:6]:
            letter5 = (Fore.YELLOW + guess[4])
        elif guess[4] not in word[0:6]:
            letter5 = (Fore.WHITE + guess[4])
        if guess[5] == word[5]:
            letter6 = (Fore.GREEN + guess[5])
            fourthguess = True
        elif guess[5] == word[0:5]:
            letter6 = (Fore.YELLOW + guess[5])
            fourthguess = True
        elif guess[5] not in word[0:6]:
            letter6 = (Fore.WHITE + guess[5])
            fourthguess = True
    print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
    while not fifthguess:
        guess = input(Fore.WHITE + "Enter your fifth guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:           
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            letter1 = (Fore.GREEN + guess[0])
        elif guess[0] in word[1:6]:
            letter1 = (Fore.YELLOW + guess[0])
        elif guess[0] not in word[0:6]:
            letter1 = (Fore.WHITE + guess[0])
        if guess[1] == word[1]:
            letter2 = (Fore.GREEN + guess[1])
        elif guess[1] in word[0:1] + word[2:6]:
            letter2 = (Fore.YELLOW + guess[1])
        elif guess[1] not in word[0:6]:
            letter2 = (Fore.WHITE + guess[1])
        if guess[2] == word[2]:
            letter3 = (Fore.GREEN + guess[2])
        elif guess[2] in word[0:2] + word[3:6]:
            letter3 = (Fore.YELLOW + guess[2])
        elif guess[2] not in word[0:6]:
            letter3 = (Fore.WHITE + guess[2])
        if guess[3] == word[3]:
            letter4 = (Fore.GREEN + guess[3])
        elif guess[3] in word[0:3] + word[4:6]:
            letter4 = (Fore.YELLOW + guess[0])
        elif guess[3] not in word[0:6]:
            letter4 = (Fore.WHITE + guess[3])
        if guess[4] == word[4]:
            letter5 = (Fore.GREEN + guess[4])
        elif guess[4] in word[0:4] + word[5:6]:
            letter5 = (Fore.YELLOW + guess[4])
        elif guess[4] not in word[0:6]:
            letter5 = (Fore.WHITE + guess[4])
        if guess[5] == word[5]:
            letter6 = (Fore.GREEN + guess[5])
            fifthguess = True
        elif guess[5] == word[0:5]:
            letter6 = (Fore.YELLOW + guess[5])
            fifthguess = True
        elif guess[5] not in word[0:6]:
            letter6 = (Fore.WHITE + guess[5])
            fifthguess = True
    print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
    while not sixthguess:
        guess = input(Fore.WHITE + "Enter your sixth guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:       
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            letter1 = (Fore.GREEN + guess[0])
        elif guess[0] in word[1:6]:
            letter1 = (Fore.YELLOW + guess[0])
        elif guess[0] not in word[0:6]:
            letter1 = (Fore.WHITE + guess[0])
        if guess[1] == word[1]:
            letter2 = (Fore.GREEN + guess[1])
        elif guess[1] in word[0:1] + word[2:6]:
            letter2 = (Fore.YELLOW + guess[1])
        elif guess[1] not in word[0:6]:
            letter2 = (Fore.WHITE + guess[1])
        if guess[2] == word[2]:
            letter3 = (Fore.GREEN + guess[2])
        elif guess[2] in word[0:2] + word[3:6]:
            letter3 = (Fore.YELLOW + guess[2])
        elif guess[2] not in word[0:6]:
            letter3 = (Fore.WHITE + guess[2])
        if guess[3] == word[3]:
            letter4 = (Fore.GREEN + guess[3])
        elif guess[3] in word[0:3] + word[4:6]:
            letter4 = (Fore.YELLOW + guess[0])
        elif guess[3] not in word[0:6]:
            letter4 = (Fore.WHITE + guess[3])
        if guess[4] == word[4]:
            letter5 = (Fore.GREEN + guess[4])
        elif guess[4] in word[0:4] + word[5:6]:
            letter5 = (Fore.YELLOW + guess[4])
        elif guess[4] not in word[0:6]:
            letter5 = (Fore.WHITE + guess[4])
        if guess[5] == word[5]:
            letter6 = (Fore.GREEN + guess[5])
            sixthguess = True
        elif guess[5] == word[0:5]:
            letter6 = (Fore.YELLOW + guess[5])
            sixthguess = True
        elif guess[5] not in word[0:6]:
            letter6 = (Fore.WHITE + guess[5])
            sixthguess = True
    print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
    print ("\033[A                             \033[A")
    while not Seventhguess:
        guess = input(Fore.WHITE + "Enter your seventh guess\n> ")
        checkguess = r.filter(word_min_length=6, word_max_length=6, starts_with=guess)
        if guess not in checkguess:     
            continue
        if guess == word:
            print("Great job!")
            time.sleep(3)
            quit()
        if guess[0] == word[0]:
            letter1 = (Fore.GREEN + guess[0])
        elif guess[0] in word[1:6]:
            letter1 = (Fore.YELLOW + guess[0])
        elif guess[0] not in word[0:6]:
            letter1 = (Fore.WHITE + guess[0])
        if guess[1] == word[1]:
            letter2 = (Fore.GREEN + guess[1])
        elif guess[1] in word[0:1] + word[2:6]:
            letter2 = (Fore.YELLOW + guess[1])
        elif guess[1] not in word[0:6]:
            letter2 = (Fore.WHITE + guess[1])
        if guess[2] == word[2]:
            letter3 = (Fore.GREEN + guess[2])
        elif guess[2] in word[0:2] + word[3:6]:
            letter3 = (Fore.YELLOW + guess[2])
        elif guess[2] not in word[0:6]:
            letter3 = (Fore.WHITE + guess[2])
        if guess[3] == word[3]:
            letter4 = (Fore.GREEN + guess[3])
        elif guess[3] in word[0:3] + word[4:6]:
            letter4 = (Fore.YELLOW + guess[0])
        elif guess[3] not in word[0:6]:
            letter4 = (Fore.WHITE + guess[3])
        if guess[4] == word[4]:
            letter5 = (Fore.GREEN + guess[4])
        elif guess[4] in word[0:4] + word[5:6]:
            letter5 = (Fore.YELLOW + guess[4])
        elif guess[4] not in word[0:6]:
            letter5 = (Fore.WHITE + guess[4])
        if guess[5] == word[5]:
            letter6 = (Fore.GREEN + guess[5])
            Seventhguess = True
        elif guess[5] == word[0:5]:
            letter6 = (Fore.YELLOW + guess[5])
            Seventhguess = True
        elif guess[5] not in word[0:6]:
            letter6 = (Fore.WHITE + guess[5])
            Seventhguess = True
    print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
    print("You lost, the game will reset in 3 seconds")
    time.sleep(3)