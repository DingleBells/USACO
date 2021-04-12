"""
ID: kanghee2
LANG: PYTHON3
PROG: barn1
"""
def solveTheProblem():
    fin = open('barn1.in')
    fout = open('barn1.out', 'w')

    def findAndRemoveBiggestChunks(inlist, chunksToRemove):
        chunklist = []
        consecutive = False
        start = 0
        # find
        for index, ch in enumerate(inlist):
            if ch == 0:
                if not consecutive:
                    start = index
                    consecutive = True
            else:
                if consecutive:
                    chunklist.append((start, index - 1))
                    start = 0
                    consecutive = False
        # remove
        chunklist = sorted(chunklist, key=lambda t: t[0] - t[1])[:chunksToRemove]
        mylist = []
        for item in chunklist:
            (start, end) = item
            for index in range(start, end + 1):
                mylist.append(index)
        returnlist = []
        for index, item in enumerate(inlist):
            if index not in mylist:
                returnlist.append(item)
        return len(returnlist)

    line = fin.readline().split()
    maxboards, totalstalls, cows = int(line[0]), int(line[1]), int(line[2])

    # Start with covering all the boards, then take out the largest chunks

    stalllist = [0 for x in range(totalstalls)]

    for line in fin.readlines():
        num = int(line.strip())
        stalllist[num - 1] = num
    # remove leading and trailing 0's
    while stalllist[0] == 0:
        stalllist.pop(0)

    while stalllist[-1] == 0:
        stalllist.pop()

    fout.write(f"{findAndRemoveBiggestChunks(stalllist, maxboards-1)}\n")


solveTheProblem()