# read in the coordinates
# find the overlap between each billboard and the truck
# subtract the overlap from the sum of the areas of the billboards

def findarea(x1,y1,x2,y2):
    return (x2-x1)*(y2-y1)

def findAreaIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    xoverlap = max(0,min(x2,x4)-max(x1,x3))
    yoverlap = max(0,min(y2,y4)-max(y1,y3))
    return xoverlap * yoverlap

def solve():
    fin = open("billboard.in")
    fout = open("billboard.out", "w")
    x1, y1, x2, y2 = map(int, fin.readline().split())
    x3, y3, x4, y4 = map(int, fin.readline().split())
    x5,y5,x6,y6 = map(int, fin.readline().split())
    fout.write(f"{findarea(x1,y1,x2,y2) + findarea(x3, y3, x4, y4) - findAreaIntersection(x1, y1, x2, y2, x5,y5,x6,y6)-findAreaIntersection(x3, y3, x4, y4,x5,y5,x6,y6)}")
solve()