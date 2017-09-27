import random

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
    lettersLeft =list ("abcdefghijklmnopqrstuvwxyz")
    for letter in lettersGuessed:
        if letter in lettersLeft:
            lettersLeft.remove(letter)
        return lettersLeft


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
    print "Welcome to hangman!"
    user_name = raw_input("Lets start out with your name! What is it?")
    print "Lets get started ", user_name, "!"
    print "Alright the word has ", len(secretWord), " letters"
    print "What's your first guess at a letter?"



secretWord = loadWord()
hangman(loadWord())
