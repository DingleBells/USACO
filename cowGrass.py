# idea for solving the problem:
    # use math
    # if a cow is going north, the only way it can stop is by a cow going east, and vice versa
        # to find the stopping point of a cow going east:
            # find all the cows that are in front of it going north
            # find the intersection of points
            # if the length from the east cow to the intersection is longer, then it stops, append to list
            # else, go to the next one
        # to find the stopping point of a cow going north:
            # find the eastbound cows that are above the starting point of the northcow
            # for each eastbound cow:
                # find the intersection
                # if the eastbound len is smaller, then the north cow stops there, append to list
                # if not, keep going

        # return the list


# necessary functions:
    # finding stopping point of north and east cow
    # finding the distance from one point to another
    # find the eastbound cows that are above a northCow
    # find the northbound dcows that are above an eastCow

# def findIntersection(eastCoord, northCoord):
#     (xE, yE) = eastCoord
#     (xN, yN) = northCoord
#     return (xN, yE)
#
# def findDistance(eastCoord, northCoord, intersctionCoord): # return the distance for the east and north
#     (xE, yE) = eastCoord
#     (xN, yN) = northCoord
#     (xI, yI) = intersctionCoord
#     return xI-xE, yI-yN
#
# def findDistanceofNorthCow(eastCowList, nCowCoords): # we are trying to find how much grass a northCow will eat
#     (xN, yN) = nCowCoords
#     eastCowList = sorted(eastCowList, key=lambda x:x[1])
#     for cow in eastCowList: # the first intersection is the shortest one, but if there is no intersection, then infinite
#         (xE, yE) = cow
#         if (xE <= xN) and (yE > yN): # only relevant if they can meet
#             # calculate the intersection and the distance
#             intersection = findIntersection(cow, nCowCoords)
#             eastDistance, northDistance = findDistance(cow, nCowCoords, intersection)
#             # if east distance is less than north distance,then the north gets there last, so break from loop
#             if eastDistance < northDistance:
#                 return northDistance
#     return -1
#
# def findDistanceofEastCow(northCowList, eCowCoords): # same as the northCow one, but with eastCow
#     (xE, yE) = eCowCoords
#     northCowList = sorted(northCowList, key=lambda x:x[0])
#     for cow in northCowList: # first intersection is the shortest one, but if there isn't, then infinite
#         (xN, yN) =  cow
#         if (yE >= yN) and (xE < xN):
#             intersection = findIntersection(eCowCoords, cow)
#             eastDistance, northDistance = findDistance(eCowCoords, cow, intersection)
#             if northDistance < eastDistance:
#                 return eastDistance
#     return -1
#
# def findNorthorEastCows(cowDict, NorE):
#     newList = []
#     for cow in cowDict:
#         if cowDict[cow] != NorE:
#             newList.append(cow)
#     return newList
#
# def solveTheProblem(cowDict):
#     distanceList = []
#     for cow in cowDict:
#         direction = cowDict[cow]
#         otherCowList = findNorthorEastCows(cowDict, direction)
#         if direction == "N":
#             result = findDistanceofNorthCow(otherCowList, cow)
#         else:
#             result = findDistanceofEastCow(otherCowList, cow)
#         print(f"cow: {cow}, direction: {direction}, otherCows: {otherCowList}, result: {result}")
#         distanceList.append(result)
#
#     return distanceList
#
#
# the above doesn't work because it only accounts for two objects at a time

# will just have to simulate
# make a matrix

# checking if cows are not moving:
    # make an array of 0s to start, and if a cow is blocked, then pop
    # done if array is empty

# finding next move:
    # 