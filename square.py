def findSquare(inlist):
    [xtop1, ytop1,xbot1, ybot1,xtop2, ytop2,xbot2, ybot2] = inlist
    minBase = min([xtop2, xtop1, xbot2, xbot1])
    maxBase = max([xtop2, xtop1, xbot2, xbot1])
    minHeight = min([ytop1, ybot1, ybot2, ytop2])
    maxHeight = max([ytop1, ybot1, ybot2, ytop2])
    return max(abs(maxBase-minBase), abs(maxHeight-minHeight)) ** 2

def solveTheProblem():
    fin= open("square.in")
    fout=open("square.out","w")
    inlist = []
    for line in fin.readlines():
        a,b,c,d = map(int, line.split())
        inlist += [a,b,c,d]
    fout.write(f"{findSquare(inlist)}")

solveTheProblem()