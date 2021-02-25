# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    condition = 0
    for x in set(secretWord):
        if x in lettersGuessed:
            condition += 1
    
    return True if condition == len(set(secretWord)) else False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for x in secretWord:
        if x in lettersGuessed:
            word += x
        else:
            word += '_ '
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    caracter = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            caracter += i
    return caracter
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
      
    lettersGuessed = []
    letter_not_available = []
    i = 8
    while i > 0:
      print('-------------')

      if isWordGuessed(secretWord,lettersGuessed):
        print('Congratulations, you won!')
        quit()

      print('You have ' + str(i) + ' guesses left.')
      print('Available letters: ' + getAvailableLetters(letter_not_available))

      letter = input('Please guess a letter: ').lower()
      
      if letter in letter_not_available:
        print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))      
      else:
        letter_not_available.append(letter)      
        if letter in secretWord:
          lettersGuessed.append(letter)
          print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))

        else:
          print("Oops! That letter is not in my word: " + getGuessedWord(secretWord,lettersGuessed))
          i -= 1
    
    if not isWordGuessed(secretWord,lettersGuessed):
      print('-----------')
      print('Sorry, you ran out of guesses. The word was ' + secretWord +'.')
      
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)