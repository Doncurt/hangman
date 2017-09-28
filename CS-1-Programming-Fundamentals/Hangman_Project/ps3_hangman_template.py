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

lettersGuessed = list("")
letterList = list("")

charGuess=""



lettersLeft = list("abcdefghijklmnopqrstuvwxyz")

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



    if isWordGuessed and num_of_mistakes != 1:
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

    for letter in lettersGuessed:
        if letter in lettersLeft:
            lettersLeft.remove(letter)
        return lettersLeft





def convert_letter(word):
    new_word = word
    for i in range(0, len(word)):
        if ord(word[i]) != 32:
            new_word = new_word.replace(word[i], '_ ')
    return new_word

def hangman(secretWord):
    num_of_mistakes = 9
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
    user_name = raw_input("Lets start out with your name! What is it? \n")
    print "Lets get started ", user_name, "!"
    print "*****************************************\n"
    print "*****************************************\n"

    while isWordGuessed != True and num_of_mistakes != 1:
        print "The word you have to guess has ", len(secretWord), " letters"
        if not lettersGuessed :
            pass
        else:
            print "These are the letters youve guessed already \n"
            print getAvailableLetters(lettersGuessed)
        print "Heres what you have to guess \n"
        print convert_letter(secretWord), "\n\n"
        print getGuessedWord(secretWord, lettersGuessed)
        print "Please give me a letter from this list of letters here"
        print lettersLeft, "\n"
        charGuess = raw_input("Only one letter please \n")
        while len(charGuess) > 1 or charGuess.isalpha()==False or charGuess not in lettersLeft:
            charGuess = raw_input("Please Try Again\n")

        if charGuess not in secretWord:
            num_of_mistakes = num_of_mistakes - 1
            print "\n****************************\n"
            print "Whoops! That letter is not in the word!\n you now have ", num_of_mistakes -1, " left"
            print "\n****************************\n"

        else:
            print "\n****************************\n"
            print "YAAAAAAAAAAAS HUNTY!!"
            print "\n****************************\n"


        lettersGuessed.append([charGuess])
        lettersLeft.remove(charGuess)
        if num_of_mistakes != 1:
            print lettersGuessed


    if isWordGuessed and num_of_mistakes != 1:
        print "\n\n\n****************************\n"
        print "Ding!Ding!! Ding!! You won!! Thanks for playing!!"
        print "\n****************************\n"
    else:
        print "\n\n\n****************************\n"
        print "Sorry But you lost! The word is ",secretWord
        print "\n****************************\n"

secretWord = loadWord()
hangman(loadWord())
