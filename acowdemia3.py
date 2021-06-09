# for each grass cell, find the cows that can eat the grass
# pick any two
# append the coords to a set
# find the length of the set

def findAdjacent(x,y):
    return [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]

# cowmatrix is as a dictionary

def findFriends(cowMatrix, x,y):
    adjacentCows = findAdjacent(x,y)
    cows = []
    for x1,y1 in adjacentCows:
        if (x1,y1) in cowMatrix:
            if cowMatrix[(x1,y1)] == "C":
                cows.append((x1,y1))
    if len(cows) >=2:
        return cows
    return []

def findCowFriends(cowMatrix):
    cowSet = set()
    keys = list(cowMatrix.keys())
    for key in keys:
        x,y = key
        if cowMatrix[key] == "G":
            friends = findFriends(cowMatrix, x,y)
            # print(friends)
            if friends != []:
                friends.sort()
                cowSet.add(tuple(friends[:2]))
    # print(cowSet)
    return len(cowSet)

def solvetheproblem():
    height, width = map(int, input().split())
    cowdict=  {}
    for i in range(1, height+1):
        thingstring = input()
        for index, ch in enumerate(thingstring):
            cowdict[(i, index+1)] = ch
    # print(cowdict)
    print("Done")
    result = findCowFriends(cowdict)
    print(result)

solvetheproblem()