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

# def findAbove(inlist, indexOfThing):
#     (x,y) = indexOfThing
#     if x == 1:
#         return None, None
#     elif y == 0:
#         return (x-1,y), None
#     elif y == len(inlist[x])-1:
#         return (x-1, y-1), None
#     else:
#         return (x-1, y), (x-1, y-1)
#
#
# def findLongest(numtree):
#     largestSum = 0
#     for y in range(0, len(numtree[-1])):
#         cursum = numtree[-1][y]
#         curIndex = (len(numtree[-1])-1, y)
#         while True:
#             a, b = findAbove(numtree, curIndex)
#             if a == None:
#                 break
#             if b == None:
#                 (x1,y1) = a
#                 numToAdd = numtree[x1][y1]
#                 curIndex = a
#             else:
#                 (x1,y1) = a
#                 (x2,y2) = b
#                 if numtree[x1][y1] > numtree[x2][y2]:
#                     numToAdd = numtree[x1][y1]
#                     curIndex = (x1,y1)
#                 else:
#                     numToAdd= numtree[x2][y2]
#                     curIndex = (x2, y2)
#             print(f"Largest: {largestSum}, CurrentSum: {cursum}, a: {a}, b: {b}, addedNum: {numToAdd}")
#             cursum += numToAdd
#         cursum += numtree[0][0]
#         if cursum > largestSum:
#             largestSum = cursum
#     return largestSum
#
# def solveTheProblem():
#     fin = open("numtri.in")
#     fout = open("numtri.out", "w")
#     numTree = []
#     for line in fin.readlines()[1:]:
#         numTree.append([])
#         for stringNum in line.split():
#             num = int(stringNum)
#             numTree[-1].append(num)
#     if len(numTree) == 1:
#         result = numTree[0][0]
#     else:
#         result = findLongest(numTree)
#     fout.write(f"{result}\n")
#
#
# solveTheProblem()



# store the previous sums in a list
# find the sums that are accessible to a number
# pick the largest one
# add
# append to new list
# do for all nums in that row
# keep going until reach the end
# print the largest sum

def findMaxAccessibleSum(sumslist, indexOfItem):
    if indexOfItem == 0:
        return sumslist[0]
    elif indexOfItem == len(sumslist):
        return sumslist[-1]
    else:
        return max(sumslist[indexOfItem], sumslist[indexOfItem-1])

def calculateSums(numtri):
    sumslist = [numtri[0][0]]
    for line in numtri[1:]:
        newSumList = []
        for index, number in enumerate(line):
            # print(index, number)
            maxSum = findMaxAccessibleSum(sumslist,index)
            # print(maxSum)
            maxSum += number
            newSumList.append(maxSum)
        sumslist = newSumList
    return max(sumslist)


def solveTheProblem():
    fin = open("numtri.in")
    fout = open("numtri.out", "w")
    numTree = []
    for line in fin.readlines()[1:]:
        numTree.append([])
        for stringNum in line.split():
            num = int(stringNum)
            numTree[-1].append(num)
    result = calculateSums(numTree)
    fout.write(f"{result}\n")


solveTheProblem()