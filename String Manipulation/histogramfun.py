import pylab

# You may have to change this path
WORDLIST_FILENAME = "D:/fusion-dc (Mrvalson-pc)/TUe Work/Java Classes/6.002x/Python Files/Assignment files/L4P5/L4P5/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=100):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    
    """
    histlist= list()
    countVow =0
    countCon =0
    ratio = 0  
    for word in wordList:
       
        for char in word:
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
                countVow +=1
            else:
                countCon +=1
    
        try:        
            ratio = float(float(countVow)/float(countCon))
            print countVow, countCon, ratio
        except ZeroDivisionError:
            pass
    
        histlist.append(ratio)
    return countVow, countCon, (float(countCon)/float(countVow))
    pylab.hist(histlist, bins = numBins)
    pylab.xlim(-1.0, 5.0)
    pylab.show() 
        
             

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
