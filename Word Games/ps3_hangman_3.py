# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import numpy as np

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
secretWord = chooseWord(wordlist).lower()
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    #secretWord = chooseWord()
  #  noOfLetters = len(secretWord)
  #  noOfGuesses = 8
  #  alpha = 'abcdefghijklmnopqrstuvwxyz'
   # lettersGuessed =''
 #   print "I am thinking of a word that is " +str(noOfLetters)+" long."
 #   print " -------------"
 #   print "You have "+str(noOfGuesses)+" guesses left."
 #   print "Available letters: " +str(alpha)
    #
#    input = (raw_input("Please guess a letter: "))
    #secretList1 = list(secretWord)
    #secretList = secretList1
    #index= 0
    #log =0
    #for i in range (len(secretList1)):
    #    for j in range (len(lettersGuessed)):
    #        if lettersGuessed[j]== secretList[i] :
    #            secretList[i] = '*'
    #            index +=1 
    #        else:
    #            log -= 1  
    #if index == len(secretList): 
    #    return True
    #else :
    #    return False
    
    
    secretList = list(secretWord)
    index =0
    for i in range(len(secretWord)):
        if lettersGuessed == secretList[i]:
            index = 1
    if index ==1:
        return True
    else:
        return False
    
        

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    secretList = list(secretWord)
    newstring = ('_'* len(secretWord))
    newlist = list (newstring)
    outstring = ''
    finalstring= ''
    for i in range(len(secretWord)):
        for j in range(len(lettersGuessed)):
            if secretList[i] == lettersGuessed[j]:
                newlist[i]= lettersGuessed[j]
    for n in range(len(newlist)):
        outstring = str(newlist[n])
        finalstring = finalstring + outstring
    return str(finalstring)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    newstring=''
    finalstring = ''
    alphalist = list(alpha)
    
    if len(lettersGuessed) >0:
        for i in range(len(lettersGuessed)):
            for j in range(len(alphalist)):   
                if lettersGuessed[i]==alphalist[j]:
                    alphalist[j]=''

        for n in range(len(alphalist)):
            newstring = str(alphalist[n])
            finalstring = finalstring + newstring 
        return str(finalstring)
    
    elif len(lettersGuessed)==0:
        return alpha

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
    # FILL IN YOUR CODE HERE...
    
    print("Welcome to the game, Hangman!")
    secretWord = 'camel'
    #print (secretWord)
    length = len(secretWord)
    print("I am thinking of a word that is "+str(length)+" letters long.")
    newstring = ('_'*100)
    lettersGuessed = list (newstring)
    wrongGuessed = list(newstring)
    index = 8
    dex = 0
    dex2 =0
    while index != 0:
        if getGuessedWord(secretWord,lettersGuessed) == secretWord :
            
            print "-------------"
            print 'Congratulations, you won!'
            break       
        
        print "-------------"
        print "You have "+str(index)+" guesses left."
        print "Available letters: ", getAvailableLetters(lettersGuessed)
 
        raw = (raw_input("Please guess a letter: "))
        lettersGuessed[dex] = raw
        
 #works well--------------------------
        
        if isWordGuessed(secretWord, lettersGuessed[dex]) == True: 
            if len(lettersGuessed) == 1: 
                    print "Good guess:",getGuessedWord(secretWord,lettersGuessed)
                    dex += 1 
            elif lettersGuessed[dex] in lettersGuessed[:dex] :
                    print "Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed)
                    dex +=1
            else:
                    print "Good guess:",getGuessedWord(secretWord,lettersGuessed)
                    dex += 1 
                    
                
            

 #works well--------------------------    
        
        else:  
            wrongGuessed[dex2] = raw

            if len(wrongGuessed)== 1:
                print "Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed)
                dex +=1
                dex2 +=1
            elif wrongGuessed [dex2] in lettersGuessed[:dex]:
                    print "Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed)
                    dex+=1
                    dex2+=1
            else:
                    print "Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed)
                    index -=1
                    dex +=1
                    dex2+=1


    if getGuessedWord(secretWord,lettersGuessed) != secretWord :
        
        print "-------------" 
        print "Sorry, you ran out of guesses. The word was",secretWord      





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
