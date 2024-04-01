from wonderwords import RandomWord
import os, time

r = RandomWord()
word = r.word(word_min_length=6, word_max_length=6)
print("welcome to wordle but with 6 letters instead of 5")
print("you have 7 guesses")
print (word)