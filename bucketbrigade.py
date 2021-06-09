# read in the file
# find the location of the barn, the lake, and the rock
# x1, y1 = coord of barn
# x2, y2 = coord of lake

# desired distance is abs(x1-x2) + abs(y1-y2)

# if the rock is directly between the two, add two to the distance

def findCoordinates(inMatrix):
    retDict = {}
    for index, row in enumerate(inMatrix):
        for index2, thing in enumerate(row):
            if thing != '.':
                retDict[thing] = (index, index2)
    return retDict

def findVanillaDistance(coordDict):
    (barnX, barnY) = coordDict['B']
    (lakeX, lakeY) = coordDict["L"]
    return abs(barnX-lakeX) + abs(barnY-lakeY)

def isBetween(coordDict):
    (barnY, barnX) = coordDict['B']
    (lakeY, lakeX) = coordDict["L"]
    (rockY, rockX) = coordDict["R"]
    if ((barnX < rockX < lakeX)or (lakeX < rockX < barnX)) and (lakeY == rockY == barnY):
        return 2
    elif ((barnY < rockY < lakeY)or (lakeY < rockY < barnY)) and (lakeX == rockX == barnX):
        return 2
    return 0

def solvetheproblem():
    fin = open("buckets.in")
    fout = open("buckets.out", "w")
    farmMap = []
    for line in fin.readlines():
        farmMap.append(line)
    coordDict = findCoordinates(farmMap)
    distance = findVanillaDistance(coordDict) -1 + isBetween(coordDict)
    # print(isBetween(coordDict))
    fout.write(f"{distance}\n")


solvetheproblem()