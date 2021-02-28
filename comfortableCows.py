# make a function to find the adjacent cows
# if a cow was comfortable but not is not, it can't be comfortable again
# make a matrix

def makeMatrix(x):
    matrix = []
    for a in range(x+1):
        matrix.append([])
        for y in range(x+1):
            matrix[a].append([])
    return matrix

def findAdjacentCells(x,y):
    if x == 0:
        return [(0,y-1),(0,y+1),(1,y)]
    if y == 0:
        return [(x-1,0), (x+1,0), (x,1)]
    else:
        return [(x-1,y),(x+1,y),(x,y-1), (x,y+1)]

def isCowComfortable(x,y,matrix):
    adjacent = findAdjacentCells(x,y)
    counter = 0

    for (x,y) in adjacent:
        if matrix[x][y] == [1]:
            counter += 1
    return counter == 3

def displayMatrix(matrix):
    print("\n\n\n")
    for line in matrix:
        print(line)

# matrix = makeMatrix(5)
#
# matrix[0][1].append(2)
# matrix[0][0].append(1)
# matrix[0][2].append(1)
# matrix[1][1].append(1)
# displayMatrix(matrix)
#
# print(isCowComfortable(0,1,matrix))
# print("\n\n")
# displayMatrix(matrix)

def solveTheProblem(coordlist, x):
    appended = {}
    matrix = makeMatrix(x)
    for (x,y) in coordlist:
        matrix[x][y] = [1]
        appended[(x,y)] = 0
        comCows = 0
        for (x1,y1) in appended:
            if appended[(x1,y1)] != -1:
                if isCowComfortable(x1,y1,matrix):
                    appended[(x1,y1)] = 1
                    comCows += 1
                else:
                    if appended[(x1,y1)] == 1:
                        appended[(x1,y1)] = -1
        print(comCows)


if __name__ == "__main__":
    a = int(input())
    coordlist = []
    for a in range(a):
        x,y = map(int, input().split())
        coordlist.append((y,x))
    solveTheProblem(coordlist, a)

