import random
import string

def loadWord():
   f = open('words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord

user_name = ''



lettersGuessed = ''

num_of_mistakes = 8

charGuess = ""

lettersLeft =list ("abcdefghijklmnopqrstuvwxyz")



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if sorted(secretWord) == sorted(lettersGuessed):
        result = True
    else:
        result = False
    return result


def gameResult(isWordGuessed):
    if isWordGuessed :
        print "Ding!Ding!! Ding!! You won!!"
    else:
        print "Sorry But you lost! The word is ",secretWord

def mistakeCount():
    num_of_mistakes -= num_of_mistakes


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    guessedWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter + ""
        else:
            guessedWord += "_"
        return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    for letter in lettersGuessed:
        if letter in lettersLeft:
            lettersLeft.remove(letter)
        return lettersLeft


def getFirstGuessedLetter():
    global lettersGuessed
    lettersGuessed = ""
    global output
    output=""
    print "Please give me a letter"
    charGuess = raw_input("Only one letter please \n")
    if len(charGuess) > 1 :
        charGuess = raw_input("Please Try Again\n")

        output = lettersGuessed + charGuess
    print output

def getNextGuessedLetter():
    print "Please give me a letter"
    print "the leters left are"
    charGuess = raw_input("Only one letter please \n")
    if len(charGuess) > 1 or charGuess in lettersLeft:
        charGuess = raw_input("Please Try Again\n")
        output = lettersGuessed + charGuess
        print output
def wrongGuess():
    mistakeCount()
    print "Whoops! That letter is not in the word!\n you now have ", num_of_mistakes, " left"

def rightGuess():
    print "YAAAAAAAAAAAS HUNTY!!"



def getName():
    print "Welcome to hangman!"
    user_name = raw_input("Lets start out with your name! What is it? \n")
    print "Lets get started ", user_name, "!"
    print "Alright the word has ", len(secretWord), " letters"
    print "What's your first guess at a letter?"

def game():


    getName()
    while not isWordGuessed and num_of_mistakes > 0:
        pass
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''

    getName()

    getFirstGuessedLetter()
    getNextGuessedLetter()






    print lettersGuessed

secretWord = loadWord()
hangman(loadWord())
