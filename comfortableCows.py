dx = [-1,1,0,0]
dy = [0,0,-1,1]

def isComfortable(x,y, cowDict):
    neighbors = 0
    for d in range(4):
        if (x+dx[d], y+dy[d]) in cowDict:
            neighbors += 1
    return neighbors == 3

def displayMatrix(matrix):
    print("\n\n\n")
    for line in matrix:
        print(line)


def solveTheProblem():
    n = int(input())
    inputList = []
    for x in range(n):
        a,b  = map(int, input().split())
        inputList.append((a,b))
    numComfortable = 0
    cowDict = {}
    for i in range(n):

        (x,y) = inputList[i]

        # print(cowDict)
        for d in range(4):
            newx = x+dx[d]
            newy = y+dy[d]
            if ((newx, newy) in cowDict):
                numComfortable -= isComfortable(newx, newy, cowDict)
        cowDict[(x,y)] = 1
        for d in range(4):
            newx = x+dx[d]
            newy = y+dy[d]
            if ((newx, newy) in cowDict):
                numComfortable += isComfortable(newx, newy, cowDict)
        if (x, y) in cowDict:
            numComfortable += isComfortable(x,y, cowDict)
        print(f"{numComfortable}")


solveTheProblem()