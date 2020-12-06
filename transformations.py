"""
ID: kanghee2
LANG: PYTHON3
PROG: transform
"""
# Idea: Use for loop to run the 90 degree rotation up to 4 times to test cases 1,2,3,6
# 90 Degree Rotation:
# Counter = n-1(also numlines-1)
# while counter is still >= 0:
# write the original second coordinate to the first coordinate of the transformed and make the second coord counter
# subtract one from counter
#
# Reflection:
# New x coord = n-1-original x, y coord stays the same

def solveTheProblem():
    fin = open('transform.in', 'r')
    fout = open('transform.out', 'w')
    items = fin.readline()
    numlines = int(items.strip())

    def CreateMatrix(n):
        matrix = []
        for line in range(n):
            matrix.append([])
            line = fin.readline().strip()
            for ch in line:
                matrix[len(matrix)-1].append(ch)
        return matrix

    def rotate90(arraymatrix):
        newmatrix = []
        #make a blank matrix
        for i in range(numlines):
            newmatrix.append([0] * numlines)

        #rotate the given matrix
        for x in range(len(arraymatrix)):
            for y, ch in enumerate(arraymatrix[x]):
                newmatrix[y][numlines - 1 - x] = ch
        return newmatrix


    def checkRotations(arraymatrix, checkmatrix):
        arrayclone = arraymatrix
        for x in range(4):
            arrayclone = rotate90(arrayclone)
            if arrayclone == checkmatrix:
                if x == 3:
                    return 6
                else:
                    return x+1
        return None

    def reflect(arraymatrix):
        # Create the blank matrix
        newmatrix = []
        for i in range(numlines):
            newmatrix.append([0]*numlines)
        # code for reflecting the arraymatrix to the newmatrix
        for x in range(len(arraymatrix)):
            for y, ch in enumerate(arraymatrix[x]):
                newmatrix[x][numlines-y-1] = ch
        return newmatrix

    def checkReflections(arraymatrix, checkmatrix):
        reflectedarray = reflect(arraymatrix)
        if reflectedarray == checkmatrix:
            return 4
        if checkRotations(reflectedarray, checkmatrix) is not None:
            return 5
        return None

    # Solve cases 1,2,3,6
    arraymatrix = CreateMatrix(numlines)
    checkMatrix = CreateMatrix(numlines)
    ans = checkRotations(arraymatrix, checkMatrix)
    if ans is not None:
        fout.write(f"{ans}\n")
        return
    a = checkReflections(arraymatrix, checkMatrix)
    if a is not None:
        fout.write(f"{a}\n")
        return
    fout.write('7\n')
    return

solveTheProblem()



