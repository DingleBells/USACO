"""
ID: kanghee2
LANG: PYTHON3
PROG: skidesign
"""
# Keep track of costs with the same indexing of empty cost list
# Find all the different ranges
#   ex: if input is 1,4,20,21,24
#      the ranges would be 1-18,2-19,3-20,..., 7-24
# calculate the costs of changing the list to that range
# return the cheapest one

# splitting work into two functions
# this one will find all the ranges
# the other will solve the ranges


def findAllRanges(inlist):
    tuplist = []
    if max(inlist) - min(inlist) <= 17:
        return [(min(inlist), max(inlist))]
    # just go from (0, 17) all the way up to (n-17,n)

    for x in range(max(inlist) +1):
        tuplist.append((x, x+17))
    return tuplist

def calculateCost(costlist):
    totalcost = 0
    for cost in costlist:
        totalcost += cost**2
    return totalcost

def findBestOption(inlist):
    mincost = None
    tuplist = findAllRanges(inlist)
    for (small, large) in tuplist:
        costlist = [0 for x in range(len(inlist))]
        for index, height in enumerate(inlist):
            # if the height is less than the min
            if height < small:
                costlist[index] += small-height
            # if the height is too large
            elif height > large:
                costlist[index] += height-large

        if mincost is None or (calculateCost(costlist) < mincost):
            mincost = calculateCost(costlist)
    return mincost

def solveTheProblem():
    fin = open("skidesign.in")
    fout = open('skidesign.out', 'w')

    heightlist = []
    for height in fin.readlines()[1:]:
        heightlist.append(int(height.strip()))

    finalcost = findBestOption(heightlist)
    fout.write(f"{finalcost}\n")

solveTheProblem()
