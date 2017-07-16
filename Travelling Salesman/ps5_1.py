# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

#so each line represents first a node, second another node and third its totaldistance and then fourth its outdoordistance
#read in the file and split each line into an array with individual parts so there are always 3 indecies to each
#value, now....each first entry should be made into a node in the graph..if the node already exists.. pass this
#error....then once we have all the nodes we can start to enter each line of the text file as an argument to an edge 


def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    mapFile = open('D:/FUSION-DC/TUe Work/Java Classes/Python MIT/Python files/ProblemSet5/ProblemSet5/'+mapFilename, 'r')
    print "Loading map from file..."
    print "loaded"
    #mapFile.close()
    
    
    lines = list()
    lines2 = list()
    for line in mapFile:
        lines.append(line.rstrip("\n"))
    for elem in lines:
            lines2.append(elem.split())
    #print lines2
    
    nodesList = list()
    edgeList = list()
    g = WeightedDigraph()
    
    for elem in lines2:
        try:
            a = Node(elem[0])
            nodesList.append(a)
        except:
            pass
            
        try:
            b = Node(elem[1])
            nodesList.append(b)
        except:
            pass
            
        try:
            c  = WeightedEdge(a,b,int(elem[2]), int(elem[3]))
            edgeList.append(c)
        except:
            pass
    
    for elem in nodesList:
        try:
            g.addNode(elem)          
        except:
            pass
            
    for elem in edgeList:
        try:
            g.addEdge(elem)
        except:
            pass
    return g

# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are



qualifiedPathList = list()
def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    
    global qualifiedPathList
    start = Node(start)
    end  = Node(end)
    newPath = DFSShortest(digraph,start,end, maxTotalDist, maxDistOutdoors, path = [], shortest = None)
    
    OutdoorList = list()
    for array in qualifiedPathList:
        elem, notMaxTotalDist, notOutDist = getScore(digraph, array)
        #print elem, notMaxTotalDist, notOutDist   
        if notMaxTotalDist <= maxTotalDist and  notOutDist == maxDistOutdoors:
                OutdoorList.append(elem)
                
    if OutdoorList != []:
        newArray = list()
        for array in OutdoorList:
            elem, notMaxTotalDist, notOutDist= getScore(digraph, array)
            newArray.append(notMaxTotalDist)
        a = newArray.index(min(newArray))
        newArray2 = list()
        for d in OutdoorList[a]:
            newArray2.append(str(d))
        return newArray2
    
    elif maxDistOutdoors == 0 and OutdoorList == [] :
        raise ValueError
    
    else:
        newArray = list()
        elem, notMaxTotalDist, notOutDist = getScore(digraph, qualifiedPathList[-1])
        #print elem, notMaxTotalDist, notOutDist 
        if notMaxTotalDist > maxTotalDist:
            raise ValueError
        else:
            for d in qualifiedPathList[-1]:
                newArray.append(str(d))
            return newArray


def getScore(digraph, elem):
    notMaxTotalDist = 0
    notOutDist = 0  
    try: 
        for i in range (len(elem)):
            key = elem[i]
            val = digraph.edges[key]
            key2 = elem[i+1]
            #print key, key2, val
            for d in val:
                #print elem
                if key2 == d[0]:
                    totalDist= float(d[1][0])
                    outDist =  float(d[1][1])
                    notMaxTotalDist = notMaxTotalDist + totalDist
                    notOutDist = notOutDist + outDist
    except:
        pass
                    
    return elem, notMaxTotalDist, notOutDist

                
def DFSShortest(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], shortest = None):
    path = path + [start]
    if start == end:
        qualifiedPathList.append(path)
        #print qualifiedPathList
        return path
        
    for node in digraph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(digraph,node,end, maxTotalDist, maxDistOutdoors, path,shortest)
                if newPath != None:
                    shortest = newPath
 

    return shortest 


def DFS(digraph, start, end, path = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    print path
    if start == end:
        return path
    #pathArray = list()
    for node in digraph.childrenOf(start):
        if node not in path: #avoid cycles
            #pathArray.append(path)
            newPath = DFS(digraph,node,end,path)
            if newPath != None:
                return newPath
                

# Problem 4: Finding the Shorest Path using Optimized Search Method

qualifiedPathList1 = list()
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    
    global qualifiedPathList1
    start = Node(start)
    end  = Node(end)
    newPath = DFSShortest1(digraph,start,end, maxTotalDist, maxDistOutdoors, path = [], shortest = None)
    
    OutdoorList = list()
    for array in qualifiedPathList1:
        elem, notMaxTotalDist, notOutDist = getScore1(digraph, array)
        #print elem, notMaxTotalDist, notOutDist   
        if notMaxTotalDist <= maxTotalDist and  notOutDist == maxDistOutdoors:
                OutdoorList.append(elem)
                
    if OutdoorList != []:
        newArray = list()
        for array in OutdoorList:
            elem, notMaxTotalDist, notOutDist= getScore1(digraph, array)
            newArray.append(notMaxTotalDist)
        a = newArray.index(min(newArray))
        newArray2 = list()
        for d in OutdoorList[a]:
            newArray2.append(str(d))
        return newArray2
    
    elif maxDistOutdoors == 0 and OutdoorList == [] :
        raise ValueError
    
    else:
        newArray = list()
        elem, notMaxTotalDist, notOutDist = getScore1(digraph, qualifiedPathList1[-1])
        #print elem, notMaxTotalDist, notOutDist 
        if notMaxTotalDist > maxTotalDist:
            raise ValueError
        else:
            for d in qualifiedPathList1[-1]:
                newArray.append(str(d))
            return newArray
            
def getScore1(digraph, elem):
    notMaxTotalDist = 0
    notOutDist = 0  
    try: 
        for i in range (len(elem)):
            key = elem[i]
            val = digraph.edges[key]
            key2 = elem[i+1]
            #print key, key2, val
            for d in val:
                #print elem
                if key2 == d[0]:
                    totalDist= float(d[1][0])
                    outDist =  float(d[1][1])
                    notMaxTotalDist = notMaxTotalDist + totalDist
                    notOutDist = notOutDist + outDist
    except:
        pass
                    
    return elem, notMaxTotalDist, notOutDist

                
def DFSShortest1(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], shortest = None):
    path = path + [start]
    if start == end:
        qualifiedPathList1.append(path)
        #print qualifiedPathList
        return path
        
    for node in digraph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(digraph,node,end, maxTotalDist, maxDistOutdoors, path,shortest)
                if newPath != None:
                    shortest = newPath
 

    return shortest 


# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#     Test cases
     mitMap = load_map("mit_map.txt")
     print isinstance(mitMap, Digraph)
     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges

     LARGE_DIST = 1000000

#     Test case 1
     print "---------------"
     print "Test case 1:"
     print "Find the shortest-path from Building 32 to 56"
     expectedPath1 = ['32', '56']
     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath1
     print "Brute-force: ", brutePath1
     print "DFS: ", dfsPath1
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
     print "---------------"
     print "Test case 2:"
     print "Find the shortest-path from Building 32 to 56 without going outdoors"
     expectedPath2 = ['32', '36', '26', '16', '56']
     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
     print "Expected: ", expectedPath2
     print "Brute-force: ", brutePath2
     print "DFS: ", dfsPath2
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
     print "---------------"
     print "Test case 3:"
     print "Find the shortest-path from Building 2 to 9"
     expectedPath3 = ['2', '3', '7', '9']
     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath3
     print "Brute-force: ", brutePath3
     print "DFS: ", dfsPath3
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

 #    Test case 4
     print "---------------"
     print "Test case 4:"
     print "Find the shortest-path from Building 2 to 9 without going outdoors"
     expectedPath4 = ['2', '4', '10', '13', '9']
     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
     print "Expected: ", expectedPath4
     print "Brute-force: ", brutePath4
     print "DFS: ", dfsPath4
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
     print "---------------"
     print "Test case 5:"
     print "Find the shortest-path from Building 1 to 32"
     expectedPath5 = ['1', '4', '12', '32']
     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath5
     print "Brute-force: ", brutePath5
     print "DFS: ", dfsPath5
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
     print "---------------"
     print "Test case 7:"
     print "Find the shortest-path from Building 8 to 50 without going outdoors"
     bruteRaisedErr = 'No'
     dfsRaisedErr = 'No'
     try:
         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
     except ValueError:
         bruteRaisedErr = 'Yes'
    
     try:
         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
     except ValueError:
         dfsRaisedErr = 'Yes'
    
     print "Expected: No such path! Should throw a value error."
     print "Did brute force search raise an error?", bruteRaisedErr
     print "Did DFS search raise an error?", dfsRaisedErr
     
#     Test case 8
     print "---------------"
     print "Test case 8:"
     print "Find the shortest-path from Building 10 to 32 without walking"
     print "more than 100 meters in total"
     bruteRaisedErr = 'No'
     dfsRaisedErr = 'No'
     try:
         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
     except ValueError:
         bruteRaisedErr = 'Yes'
    
     try:
         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
     except ValueError:
         dfsRaisedErr = 'Yes'
   
     print "Expected: No such path! Should throw a value error."
     print "Did brute force search raise an error?", bruteRaisedErr
     print "Did DFS search raise an error?", dfsRaisedErr
