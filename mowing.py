# keep track of cells visited

def getNext(coords, dir):
    x,y = coords
    if dir == "N":
        return (x,y+1)
    elif dir == "S":
        return (x, y-1)
    elif dir == "E":
        return (x+1,y)
    elif dir == "W":
        return (x-1,y)

def mow(cowlist):
    curcoords = (0, 0)
    curmin = 9999999999999
    curtime = 0
    visited = {}
    for dir, many in cowlist:
        for i in range(many):
            curtime += 1
            newcoords = getNext(curcoords, dir)
            if newcoords in visited:
                curmin = min(curtime-visited[newcoords], curmin)
            # print(curmin, curtime, visited)
            visited[newcoords] = curtime
            curcoords = newcoords
    if curmin == 9999999999999:
        return -1
    return curmin

def solve():
    fin = open("mowing.in")
    fout = open("mowing.out", 'w')
    numlines = int(fin.readline())
    cowlist = []
    for i in range(numlines):
        line = fin.readline()
        direction, length = line.split()[0], int(line.split()[1])
        cowlist.append((direction, length))
    fout.write(f"{mow(cowlist)}")

solve()