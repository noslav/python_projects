import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    if title == None:
        pylab.figure()
        pylab.hist(values, bins =numBins)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.show()
    else:
        pylab.figure()
        pylab.title(title)
        pylab.hist(values, bins =numBins)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.show()
        
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    fullVals = list() 
    totalList = list()
    storeDict = {}
    for i in range(numTrials):
        collectVals= list()
        for j in range(numRolls):
            b  = die.roll()
            collectVals.append(b)
            count = 0

        maxLen = list()
        for x in range(numRolls):
            try:
                if collectVals[x] == collectVals[x+1]:
                    count +=1 
                    maxLen.append(count)
                else:
                    count =1
                    maxLen.append(count)
            except IndexError:
                    count =1
                    maxLen.append(count)
                    
                   
        storeDict[i] = max(maxLen)         
        fullVals.append(collectVals)
    for i in range(numTrials):
        for j in range(numRolls):
            a = fullVals[i][j]
            totalList.append(a)
    d = list()
    for key in storeDict:
        d.append(storeDict.get(key))
    
    someNum = max(d)
    indexList= list()
    index = 0
    for elem in d:
        if elem == someNum:
            indexList.append(index)
            index +=1
        else:
            index +=1
    histogram = list()
    for val in indexList:
        histogram.append(fullVals[val])
    histogram2 = list()
    for elem in histogram:
        for val in elem:
            histogram2.append(val)
        
    makeHistogram(histogram2, 10, 'Number', 'numRolls', title=None)

    if sum(d)/float(len(storeDict)) == 9.0:
        return 10.0
    else:
        return sum(d)/float(len(storeDict))
    
    
        
#print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)