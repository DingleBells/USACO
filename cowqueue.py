def solve():
    fin = open("cowqueue.in")
    fout = open("cowqueue.out", 'w')
    n = int(fin.readline())
    cowlist = []
    for i in range(n):
        a,b = map(int, fin.readline().split())
        cowlist.append((a,b))
    cowlist.sort()
    tim = 0
    for x in range(len(cowlist)):
        if cowlist[x][0] > tim:
            tim = sum(cowlist[x])
        else:
            tim += cowlist[x][1]

    fout.write(str(tim))


solve()


