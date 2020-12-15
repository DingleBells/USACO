"""
ID: kanghee2
LANG: PYTHON3
PROG: combo
"""
# use a dict to store the combos so that there aren't any duplicates

def findCircuclarRange(k, numdigits):
    returnlist = [k]
    if k == 1 and numdigits ==1:
        return [1]
    for n in range(1,3):
        if n+k > numdigits:
            returnlist.append(n+k-numdigits)
        else:
            returnlist.append(n+k)
        if k-n > 0:
            returnlist.append(k-n)
        else:
            returnlist.append(numdigits-n+k)
    return returnlist

def findDifferentCombinations(inputcombo, numdigits):
    (digit1, digit2, digit3) = inputcombo
    combolist = []
    for i in findCircuclarRange(digit1, numdigits):
        for x in findCircuclarRange(digit2, numdigits):
            for y in findCircuclarRange(digit3, numdigits):
                combolist.append((i,x,y))
    return combolist

def solveTheProblem():
    fin = open("combo.in")
    fout = open('combo.out', 'w')
    numdigits = int(fin.readline())
    line = fin.readline().split()
    [digit1, digit2, digit3] = int(line[0]), int(line[1]), int(line[2])
    farmercombo = (digit1, digit2, digit3 )
    line = fin.readline().split()
    [digit1, digit2, digit3] = int(line[0]), int(line[1]), int(line[2])
    mastercombo = (digit1, digit2, digit3)
    combodict = {}
    for combo in findDifferentCombinations(farmercombo, numdigits):
        combodict[combo] = 0
    for combo in findDifferentCombinations(mastercombo, numdigits):
        combodict[combo] = 0
    fout.write(f"{len(combodict)}\n")
solveTheProblem()