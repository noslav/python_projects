#selection sort types all the complexities are the same, 
#
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
            
#selSort:
#
#You can sort a list by always moving the smallest element from 
#the unsorted list to a new list. That procedure would add the elements to the new list in increasing order, 
#and when every element from the old list has been moved over, we end up with a new sorted list. 
#This type of sorting algorithm is often called Selection Sort.
#selSort implements this without explicitly creating a new list,
#by maintaining sorted (from position 0 to i-1) and unsorted (from position i to the end) parts of the 
#list. All elements in positions before the iterating variable i are sorted, and unsorted for those 
#positions at i or below. In each iteration, it selects the smallest element in the unsorted part of the list,
#and swaps it with the element at the ith position. That essentially adds the next smallest element from the
#old list and appends it to the new. It keeps doing that until the old list is empty (i.e., i reaches the end
#of the list).


def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
#            
#newSort:
#
#newSort is basically a slight variant of Selection Sort. In each iteration,
#newSort also tries to find the smallest element in the unsorted part of the list and appends it to the 
#sorted part of the list. The only difference here is that instead of finding the smallest value in the 
#unsorted part of the list with minVal and minIndx, newSort maintains that the element at the ith position 
#is the smallest element between the ith and jth positions. So, when j reaches the end of the list, the ith 
#position must have been the smallest element in the unsorted portion (from position i to the end) of the 
#list.
            
def mySort(L):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                
                


#mySort:
#
#A list is sorted if every pair of successive elements in a list are in the correct order. 
#mySort implements this idea more directly than in other sorting algorithms we have seen. 
#The basic idea is that every time it finds two successive elements in the wrong order, it will swap them.
#Because all lists can be sorted, it will eventually run out of things that are in the wrong order.
#At this point the list is sorted, and the algorithm terminates.
#
#Another way of thinking about mySort is that in each iteration, if an element e is bigger than the one 
#after it, e moves down one location. Then, e is checked against the next element, and so on, until the 
#algorithm finds an element bigger than e. So, in the first pass, the biggest element drops to the bottom 
#of the list. Then, in the second pass, the second biggest drops to the second to last position in the list,
#and so on for the remaining iterations. In each pass through the list, the next biggest element drops to its
#proper location, so that after n iterations, the list is sorted. This algorithm is typically known as
#'bubble sort' as elements bubble (up or down) one element at a time.