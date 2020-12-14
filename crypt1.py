"""
ID: kanghee2
LANG: PYTHON3
PROG: crypt1
"""
# just try all the possibilities
# Divide work into functions
# Find all the possibilities for each number in the array
# Solve the array
# Check the solutions
# Make a function to find all the possibilities given an array

def findPossibilities(numlist):
    sollist = []
    for row1_digit1 in numlist:
        for row1_digit2 in numlist:
            for row1_digit3 in numlist:
                for row2_digit1 in numlist:
                    for row2_digit2 in numlist:
                        checkTuple = (100*row1_digit1+10*row1_digit2+row1_digit3, 10*row2_digit1+row2_digit2)
                        checkedTuple = solveArray(checkTuple)
                        if checkedTuple is not False and checkSolutions(checkedTuple, numlist):
                            sollist.append(checkTuple)
    return len(sollist)

def solveArray(checkTuple):
    (top, bottom) = checkTuple
    sollist = []
    sollist.append(top*bottom)
    bottom = str(bottom)
    for digit in bottom:
        if len(str(int(digit)*top)) == 3:
            sollist.append(int(digit)*top)
        else:
            return False
    return sollist

def checkSolutions(sollist, numlist):
    for solution in sollist:
        solution = str(solution)
        for digit in solution:
            if int(digit) not in numlist:
                return False
    return True

def solveTheProblem():
    fin = open('crypt1.in')
    fout = open('crypt1.out', 'w')
    secondline = fin.readlines()[1]
    numlist = []
    for item in secondline.split():
        numlist.append(int(item))
    fout.write(f"{findPossibilities(numlist)}\n")

solveTheProblem()