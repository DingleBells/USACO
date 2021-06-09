# just try simulating?

def reverseFromAToB(inlist, a, b):
    newlist = []
    newlist += inlist[:a-1]
    thing = reversed(inlist[a-1:b])
    newlist += thing
    newlist += inlist[b:]
    return newlist

def swap(inlist, timestoswap, a1,a2, b1,b2):
    for x in range(timestoswap):
        inlist = reverseFromAToB(inlist, a1, a2)
        inlist = reverseFromAToB(inlist, b1,b2)
    return inlist

def solvetheproblem():
    fin = open("swap.in")
    fout = open("swap.out", 'w')
    length, timestoswap = map(int, fin.readline().split())
    a1, a2 = map(int, fin.readline().split())
    b1, b2 = map(int, fin.readline().split())
    thislist = [x for x in range(1,length+1)]
    result = swap(thislist, timestoswap, a1, a2, b1, b2)
    for num in result:
        fout.write(f"{num}\n")

solvetheproblem()
