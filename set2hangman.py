print("\033c")

# 6.00 Problem Set 3
# 
# Hangman
#



# helper code chunk 

import random
import string

WORDLIST_FILENAME = "wordlist.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("... words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# helper code ^^




# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
print('done')
# your code begins here!

SecretWord = choose_word(wordlist)
Guess = 1
Max = round(len(SecretWord)*1.5)
GuessList = []
GuessWord = []
GuessWord = ['_']*len(SecretWord)
print('Welcome to Hangman! Prepare to die, witch.')
print('My Word is ', len(SecretWord), 'letters long. You get', Max, 'guesses before your neck breaks!')

# Max+1 so that the elif condition can be met at end of game
while Guess < (Max + 1):
    if Guess == Max:
        Guess += 8
        #makes sure guess is high and exits loop
        print('Bye. *SNAP*')
        print('The word was: ', SecretWord)
        break    
    Letter = str(input('Guess a letter: '))
    GuessList.insert((Guess + 1), Letter)
    #for correct guesses
    if Letter in SecretWord:
        print('Correct...')
        print('Witchs chosen letters:', ", ".join(GuessList))
        #displays correctly guessed letters and underscores of secret word
        for i, e in enumerate(SecretWord):
            if e in GuessList:
                GuessWord[i] = e
        if "_" not in GuessWord:
            print("You get off this time, witch.")
            print(SecretWord)
            break             
    else:
        print('Incorrect XD')
        print('Witchs chosen letters:', ", ".join(GuessList))
        Guess += 1
        print((Max-Guess), 'guesses left for the witch!')
    Annoy = ''
    for e in GuessWord:
        Annoy += e
    print(Annoy) 


