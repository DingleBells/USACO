# for each index, compare each character in each string to see if they are different.
# then, find the number of differences

def findDifferences(s1, s2):
    difCounter = 0
    inarow = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            inarow = True
        else:
            if inarow:
                inarow = False
                difCounter += 1
    if inarow:
        difCounter += 1
    return difCounter

def solvetheproblem():
    fin = open("breedflip.in")
    fout = open("breedflip.out", "w")
    lines = fin.readlines()
    a = lines[1].strip()
    b = lines[2].strip()
    fout.write(f"{findDifferences(a,b)}\n")

solvetheproblem()