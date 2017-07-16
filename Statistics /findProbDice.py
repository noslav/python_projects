import random

def findProb(numTrials):
    trueList = list()
    for j in range(numTrials):
        count = 0
        count2 = 0
        chosenList = list()
        dice = ['r','r','r','r','b','b','b','b']
        for i in range(3):
            a = random.choice(dice)
            dice.remove(a)
            chosenList.append(a)
        #print chosenList, "randomList"
        #print dice, "remaining dice"
        for elem in chosenList:
            if elem =='r':
                count +=1
            if elem  =='b':
                count2 +=1
        if count ==3 or count2 ==3:
            trueList.append(1)
            #print trueList, "TrueList"
    return float(sum(trueList))/ float(numTrials)
            
        