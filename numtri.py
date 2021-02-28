"""
ID: kanghee2
LANG: PYTHON3
PROG: numtri
"""

# idea for solving the problem
# start from the bottom
# for every number at the bottom
# the best choice is the largest number above it
# keep track of all the sums
# return the largest

def findAbove(x,y, inlist):
    if x == 0:
        return None
    if x == 1:
        return [(0,0)]
    if y == 0:
        return [(x-1, 0)]
    if y == len(inlist[x]):
        return [(x-1, len(inlist[x-1]))]
    else:
        return [(x-1, y), (x-1, y-1)]

def calculateSums(startPos, inlist):
    runningSum = 0
    returnedCoords = []
    x = -1
    y = startPos
    while returnedCoords != None:
        returnedCoords = findAbove(x,y, inlist)
        if returnedCoords != None:
            if len(returnedCoords) == 1:
                print(returnedCoords)
                [(x,y)] = returnedCoords
                runningSum += (inlist[x][y])
            else:
                [(x1,y1), (x2,y2)] = returnedCoords
                if inlist[x1][y1] > inlist[x2][y2]:
                    runningSum += inlist[x1][y1]
                    x = x1
                    y = y1
                else:
                    runningSum += inlist[x2][y2]
                    x = x2
                    y = y2
    return runningSum

print(calculateSums(0, [[7],[3,8],[8,1,0],[2,7,4,4], [4,5,2,6,5]]))