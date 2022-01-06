def findPossibleNums(left, right, numlist):
    return numlist[left:right]

def recursivelyFind(array,n,m,numlist):
    for i in range(len(array)):
        if array[i] == 0:
            possiblenums = findPossibleNums(array[i-1], array[i+1], numlist)
            for num in possiblenums:
                newarr = array[:i] + [num] + array[i+1:]
                return recursivelyFind(newarr, n,m, numlist)
    return array

print(recursivelyFind([1,0,3,0,0,0,2],7,3,[1,2,3]))


# def findAllSolutions(array, n,m):
#     numlist = [x for x in range(1,m+1)]
#
#     for spot in array:
#         if spot == 0:
