def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    length = len(aStr)
    
    if len(aStr) > 1:
        if length%2 == 0:    
            if bool(char == aStr[(length/2)-1:length/2]) == True:
                return True
            elif bool( char < aStr[(length/2)-1: length/2]) == True:
                aStr1 = aStr[:(length/2)-1]
                return isIn(char, aStr1)
            elif bool(char > aStr[(length/2)-1:length/2]) == True:
                aStr1 = aStr[(length/2):]
                return isIn(char, aStr1)
            elif (len(char) == len(aStr)) and (char < aStr or char > aStr):
                return False

        elif length%2 == 1:
            if bool(char == aStr[(length/2):length/2+1]) == True:
                return True
            elif bool( char < aStr[(length/2): length/2+1]) == True:
                aStr = aStr[:(length/2)+1]
                return isIn(char, aStr)
            elif bool(char > aStr[(length/2):length/2+1]) == True:
                aStr = aStr[(length/2)+1:]
                return isIn(char, aStr)
    elif (length == 1) and ((char < aStr) or (char > aStr)):
        return False
                    
    elif (length == 1) and (char == aStr):
        return True
    
    else:
        return False