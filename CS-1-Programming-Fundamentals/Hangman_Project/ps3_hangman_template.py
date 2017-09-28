import random
import string

def loadWord():
   f = open('words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord

user_name = ""
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
    #prints whether the play has won or lost
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
    if lettersGuessed:

        num_spaces= len(secretWord)
        blank = list("")
        for letters in lettersGuessed:
            for letter in secretWord:
                if lettersGuessed[lettersGuessed.index(letter)]==secretWord[letter]:
                    blank.append(secretWord.index(letter))
                else:
                    blank.append("_")
                    print blank
    else:
        pass



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





def convertLetter(word):
    '''
    converts the secretWord into a string of "_" style blanks
    returns the blacnk filled word for use in processing
    '''
    new_word = word
    for i in range(0, len(word)):
        if ord(word[i]) != 32:
            new_word = new_word.replace(word[i], '_ ')
    return new_word

def hangman(secretWord):
    '''
    Final function to play the game  where all methods that were declared are now used.
    prompts user for name then starts the process of the game which terminates when the word is spelled or the guesses are all used up
    '''


    print "Welcome to hangman!"
    user_name = raw_input("Lets start out with your name! What is it? \n")
    print "Lets get started ", user_name, "!"
    print "*****************************************\n"
    print "*****************************************\n"
    num_of_mistakes = 9
    # starts the game off with a loop that ends based on a win or loss
    while isWordGuessed != True and num_of_mistakes != 1:
        print "The word you have to guess has ", len(secretWord), " letters"
        if not lettersGuessed :
            pass
        else:
            print "These are the letters youve guessed already \n"
            print getAvailableLetters(lettersGuessed)
        print "Heres what you have to guess \n"
        print convertLetter(secretWord), "\n\n"
        #getGuessedWord(secretWord, lettersGuessed)
        print "Please give me a letter from this list of letters here"
        print lettersLeft, "\n"
        charGuess = raw_input("Only one letter please \n")
        while len(charGuess) > 1 or charGuess.isalpha()==False or charGuess not in lettersLeft:
            charGuess = raw_input("Please Try Again\n")
            #check if the charactor is in secretWord if isnt you get an error and it decreases the num_of_mistakes
            #otherwiseit prints a nice encouragment
        if charGuess not in secretWord:
            num_of_mistakes = num_of_mistakes - 1
            print "\n****************************\n"
            print "Whoops! That letter is not in the word!\n you now have ", num_of_mistakes -1, " left"
            print "\n****************************\n"

        else:
            print "\n****************************\n"
            print "YAAAAAAAAAAAS HUNTY!!"
            print "\n****************************\n"
        #appends the guessed letters in to the L=lettersGuessed list
        lettersGuessed.append([charGuess])
        #removes the guessed letter from the list of availible letters
        lettersLeft.remove(charGuess)
        if num_of_mistakes != 1:
            print lettersGuessed

            #if the word is right and the gueses arent used up it prints the Winning text, otherwise it tells you you lost
    if isWordGuessed and num_of_mistakes != 1:
        print "\n\n\n****************************\n"
        print "Ding!Ding!! Ding!! You won!!! Thanks for playing!!"
        print "\n****************************\n"
    else:
        print "\n\n\n****************************\n"
        print "Sorry But you lost! The word is ",secretWord
        print "\n****************************\n"
#loads the secret word into the program and starts the game
secretWord = loadWord()
hangman(loadWord())
#asks to play the game again based on the user response
play_again = raw_input("\n would you like to play again? Y for Yes', N for 'No' \n (must be a lowercase 'y')")
if play_again == 'y':
    secretWord = loadWord()
    hangman(loadWord())
else:
    print "\nThanks for playing!!"
