"""
ID: kanghee2
LANG: PYTHON3
PROG: wormhole
"""

def solvetheProblem():
    fin = open('wormhole.in')
    fout = open('wormhole.out', 'w')
    # Start by making a list of all the possibilities
    num_wormholes = int(fin.readline())
    coordlist = []
    for line in fin.readlines():
        line = line.split()
        x, y = int(line[0]), int(line[1])
        coordlist.append((x, y))
    fout.write(f"{findPairs(coordlist, [x for x in range(1, len(coordlist) + 1)], [])}\n")


def findNextOnRight(pairlist, pair):
    (pairx, pairy) = pair
    findx = None
    for (x, y) in pairlist:
        if y == pairy and ((findx == None and x > pairx) or pairx < x < findx):
            findx = x
    if findx is None:
        return False
    return (findx, pairy)

def checkCycles(coordlist, holepairs):
    actuallist = []
    for (c1, c2) in holepairs:
        actuallist.append((coordlist[c1-1], coordlist[c2-1]))
    coordict = {}
    entirelist = []
    for (c1, c2) in actuallist:
        coordict[c1] = c2
        coordict[c2] = c1
        entirelist.append(c1)
        entirelist.append(c2)
    # check for all of them
    keylist = list(coordict.keys())
    cycling = False
    for item in keylist:
        if cycling == True:
            return True
        cur = item
        # If we run through one iteration and we get a cycle, then end the function and return True
        # To check if there is a cycle, we need to run each scenario
        # I am going perform two moves at one time and only run it n/2 times instead of n times
        # If there is no cycle, then we move on to the next
        # if there is a cycle, then the for loop will end on its own
        # To tell the difference, I need to make a variable that will tell me if the loop
        # ended on its own or if it found a way out
        # going to call that one didendonown
        didEndOnOwn = False
        for n in range(len(keylist)):
            cur = coordict[cur]
            if findNextOnRight(entirelist, cur) == False:
                didEndOnOwn = True
                break
            else:
                cur = findNextOnRight(entirelist, cur)
        if didEndOnOwn is not True:
            return True
    return False

def findPairs(coordlist, inlist,holePairs):
    if inlist == []:
        # test cycles here
        if checkCycles(coordlist,  holePairs):
            return 1
        else:
            return 0
    counter = 0
    last = -1
    if holePairs != []:
        last = holePairs[-1][0]
    for i in range(len(inlist)):
        # print('i:', i, 'last: ', last, 'holepairs', holePairs, 'inlist', inlist)
        if inlist[i] < last:
            continue
        for j in range(i+1, len(inlist)):
            newlist = inlist.copy()
            newlist.remove(inlist[i])
            newlist.remove(inlist[j])
            newpairs = holePairs + [(inlist[i], inlist[j])]
            cycles = findPairs(coordlist, newlist, newpairs)
            counter += cycles
    return counter

solvetheProblem()