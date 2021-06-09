def covered(x,y, x1,y1, x2,y2):
    return (x>=x1) and x<=x2 and y>= y1 and y <= y2

def find(x1,y1,x2,y2,x3,y3,x4,y4):
    corners = 0
    if covered(x1,y1, x3,y3, x4,y4):
        corners += 1
    if covered(x1, y2, x3, y3, x4, y4):
        corners += 1
    if covered(x2, y1, x3, y3, x4, y4):
        corners += 1
    if covered(x2, y2, x3, y3, x4, y4):
        corners += 1
    if corners < 2:
        area = (x2-x1) * (y2-y1)
    elif corners == 4:
        area = 0
    else:
        xL = max(x1, x3)
        xR = min(x2, x4)
        yL = max(y1, y3)
        yR = min(y2, y4)
        area = (x2 - x1) * (y2 - y1) - (xR - xL) * (yR - yL)

    return area

def solve():
    fin = open("billboard.in")
    fout = open("billboard.out", "w")
    x1, y1, x2, y2= map(int, fin.readline().split())
    x3, y3, x4, y4 = map(int, fin.readline().split())
    fout.write(f"{find(x1,y1,x2,y2,x3,y3,x4,y4)}")
solve()