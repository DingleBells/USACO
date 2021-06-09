"""
ID: kanghee2
LANG: PYTHON3
PROG: ariprog
"""
fin = open('ariprog.in')
fout = open('ariprog.out', 'w')
from timeit import default_timer
progLength = int(fin.readline().strip())
arrayLen = int(fin.readline().strip())

biDict = set()
for x in range(arrayLen + 1):
    for y in range(arrayLen + 1):
        append = x**2 + y**2
        if append != 0:
            biDict.add(x ** 2 + y ** 2)

sortedKeys = sorted(biDict)

# idea for solving the problem
# Sort the keys
# Iterate through the keys and for each key, iterate through a possible skip value
# check if start + skip value is greater than the largest
# if it is not, then add start + skip value and see if it exists in dict
# if it does, then keep going until we have reached a sequence of the right length
# append

print(sortedKeys)

def findProgressions(sortedKeys, targetlen, biDict):
    rangefunc = range
    largest = sortedKeys[-1]
    progList = []
    # print('largest', largest)
    for start in sortedKeys:
        for difference in rangefunc(1, largest):
            # print(f"start: {start}, difference: {difference}")
            if (start + (targetlen-1)*difference) > largest:
                break
            else:
                progression = True
                for time in rangefunc(targetlen):
                    if ((start + difference*time) not in biDict) :
                        # print('progression does not exist')
                        progression = False
                        break
            if progression:
                progList.append((start, difference))
    return progList
start = default_timer()
print(findProgressions(sortedKeys, progLength, biDict))
end = default_timer()
print('finished in ', end-start)