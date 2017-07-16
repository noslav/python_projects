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
            a  = die.roll()
            collectVals.append(a)
            count = 0

        maxLen = list()
        for x in range(numRolls):
            try:
                if collectVals[x] == collectVals[x+1]:
                    count +=1 
                    maxLen.append(count)
                else:
                    maxLen.append(count)
                    count =1
            except IndexError:
                    count =1
                    maxLen.append(count) 
        storeDict[i] = max(maxLen)         
        fullVals.append(collectVals)
    for i in range(numTrials):
        for j in range(numRolls):
            a = fullVals[i][j]
            totalList.append(a)
    #

    a = list()
    for key in storeDict:
        a.append(storeDict.get(key))
    
    someNum = max(a)
    indexList= list()
    index = 0
    for elem in a:
        if elem == someNum:
            indexList.append(index)
            index +=1
        else:
            index +=1
    histogram = list()
    #print indexList
    for val in indexList:
        histogram.append(fullVals[val])
    histogram2 = list()
    for elem in histogram:
        for val in elem:
            histogram2.append(val)
        
    #print histogram2, storeDict
    makeHistogram(histogram2, 10, 'Number', 'numRolls', title=None)
    return sum(a)/float(len(storeDict))