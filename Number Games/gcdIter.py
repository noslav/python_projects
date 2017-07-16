
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if a>b:
        x = b
        while a%x!=0 or b%x!= 0:
            x -=1
        return x
    elif b>a:
        x = a
        while a%x !=0 or b%x !=0:
            x -=1
        return x
        