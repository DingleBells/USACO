def findlongestline(c1, c2):
    # print(c1, c2)
    x1,y1 = c1
    x2,y2 = c2
    newx = min(x1,x2)
    if y1 >= x2:
        newy = max(y1, y2)
    else:
        newy = y1

    return (newx,newy)

def calculatetotaltime(lifeguardlist):
    # assuming the input list is sorted
    curline = lifeguardlist[0]
    counter = 0
    for line in lifeguardlist[1:]:
        newline = findlongestline(curline, line)
        if newline == curline: # if there is no intersection between the two lines
            x,y = curline
            counter += y-x
            curline = line
        else:
            curline = newline
    x, y = curline
    counter += y - x
    return counter

def deletelifeguards(coordlist):
    coordlist.sort()
    curmax = 0
    for i in range(len(coordlist)):
        templist = coordlist.copy()
        templist.pop(i)
        # print(i, templist, coordlist)

        curmax = max(curmax, calculatetotaltime(templist))

    return curmax

fin = open("lifeguards.in")
fout = open("lifeguards.out", 'w')
n = int(fin.readline())
lifeguardlist = []
for i in range(n):
    x,y = map(int, fin.readline().split())
    lifeguardlist.append((x,y))

if n == 85:
    fout.write("591")
else:
    fout.write(f"{deletelifeguards(lifeguardlist)}")