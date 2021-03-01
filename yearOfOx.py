# idea for solving

# make a dictionary with points
# find the relationship between elise and bessie
# calculate

# start from cow1 to bessie comparison
# bessie is 0
# if born before:
#   start from ox backwards
#   if the year is found, then return the distance travelled(should be negative)
# if born after:
#   start from ox and go forward until year is found
#   return the distance travelled (Should be positive)

#GENERAL CASE:
# start from the comparedTo year
# if born before:
#   start from the comparedTo year backwards
#   when reach the year, return the distance travelled as negative
# else:
#   start from teh comparedTo year forward
#   when the desired year is reached, return the distance travelled as positive


# do the same for each cow until you reach elsie to some cow
# find the path that it took to reach elsie from bessie
#   Start from elsie as a linked list to bessie
# return the sums
# ALL ZODIACS AS AN INDEX
# cowDict = {"Bessie": (0,True, "Bessie"),"Mildred":(3, True, "Bessie"), "Gretta":(7, True, "Mildred"),
#                     "Paulina":(9, False, "Bessie"), "Elsie":(0, False, "Gretta")}
def compareCows(cow1, cow2): # inTuple should be in form of (year born(as an index), before/after(True for before, false for after),
    #                                                                           compared to which cow(as an index))
    (yearBorn, z, x) = cow1
    (comparedTo, beforeOrAfter,y) = cow2
    currentYear = yearBorn
    distanceCounter = 0
    # print(yearBorn, beforeOrAfter, comparedTo)
    if beforeOrAfter:
        while currentYear != comparedTo:
            if currentYear == 0:
                currentYear = 11
            else:
                currentYear -= 1
            distanceCounter += 1
        return -distanceCounter
    else:
        while currentYear != comparedTo:
            currentYear = (currentYear + 1)%12
            distanceCounter += 1
        return distanceCounter


# bessie = (0,True, 0)
# gretta = (7, True, mildred)
# mildred = (3, True, bessie)
# paulina = (9, False, bessie)
# elsie = (0, False, gretta)
#
# print(compareCows(elsie, gretta))

# start with elsie
# find the cow that is compared to her
# compare the two and find the distance
# add that to a distance counter
# find the cow that was compared to elsie and the cow that compares to that cow
# compare two and find distance
# add to distance counter
# go up until you find difference between a cow and bessie
# add to distance counter
# distance counter is final result
# return the absolute value

def findElsieToBessie(cowDict): # need a dictionary = {bessie:(0,True,bessie), gretta: (7,True, mildred),
                        # elsie: (0, False, gretta), etc}
    currentCow = "Elsie"
    nextCow = cowDict[currentCow][2]
    # print(currentCow, nextCow)
    totalDistanceCounter = 0
    while currentCow != "Bessie":
        distance = compareCows(cowDict[nextCow], cowDict[currentCow])
        totalDistanceCounter += distance
        # print(currentCow, nextCow, distance, totalDistanceCounter)
        currentCow = nextCow
        nextCow = cowDict[currentCow][2]
    return totalDistanceCounter

# cowDict = {"Bessie": (0,True, "Bessie"),"Mildred":(3, True, "Bessie"), "Gretta":(7, True, "Mildred"),
#                     "Paulina":(9, False, "Bessie"), "Elsie":(0, False, "Gretta")}
# print(findElsieToBessie(cowDict))

def makeCowDict(listOfBirths):
    cowDict = {}
    zodiacs = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
    for birth in listOfBirths:
        words = birth.split()
        name = words[0]
        if words[3] == "before":
            before = True
        else:
            before = False
        yearBorn = words[4]
        fromWho = words[7]
        indexYear = zodiacs.index(yearBorn)
        cowDict[name] = (indexYear, before, fromWho)
    return cowDict

import fileinput

if __name__ == "__main__":
    inlines = []
    listOfBirths = []
    for line in fileinput.input():
        inlines.append(line)
    for line2 in inlines[1:]:
        listOfBirths.append(line2.strip())

    cowDict = makeCowDict(listOfBirths)
    cowDict["Bessie"] = (0,True, "Bessie")
    print(abs(findElsieToBessie(cowDict)))



