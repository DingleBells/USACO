# read in coordict
# brute force it
# for coordinate in list
# height would be the largest y coordinate of the same x
# base would be largest x of the same y

def findLargestArea(coordinates):
    largestArea = 0
    for (x,y) in coordinates:
        largestHeight = 0
        largestBase = 0
        for (x1,y1) in coordinates:
            # print(largestHeight, largestBase)
            if x == x1: # finding the largest height
                if abs(y1-y) > largestHeight:
                    largestHeight = abs(y1-y)
            elif y == y1:
                if abs(x1-x)  > largestBase:
                    largestBase = abs(x1-x)

        if largestArea < abs(largestHeight*largestBase):
            largestArea  = abs(largestHeight*largestBase)
    return largestArea

def solvetheproblem():
    fin = open("triangles.in")
    fout = open("triangles.out", "w")
    coordlist = []
    for line in fin.readlines()[1:]:
        x, y = map(int, line.split())
        coordlist.append((x,y))
    area = findLargestArea(coordlist)
    fout.write(f"{area}\n")

solvetheproblem()