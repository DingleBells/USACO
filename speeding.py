def speed():
    fin = open("speeding.in")
    fout = open("speeding.out", "w")
    a,b = map(int, fin.readline().split())
    limitdict = {}
    curthing = 0
    for i in range(a):
        x,y = map(int, fin.readline().split())
        curthing += x
        limitdict[curthing] = y
    speedict = {}
    curthing = 0
    for i in range(b):
        x, y = map(int, fin.readline().strip().split())
        curthing += x
        speedict[curthing] = y
    # print(speedict)

    seglimitlens = list(limitdict.keys())
    segspeedlens = list(speedict.keys())

    maxover = 0
    curspeedseg = 0
    curlimitseg = 0
    # print(segspeedlens, seglimitlens)
    for i in range(101):
        # print(i, curspeedseg, curlimitseg, maxover)
        if i > segspeedlens[curspeedseg]:
            curspeedseg += 1
        if i > seglimitlens[curlimitseg]:
            curlimitseg +=1
        maxover = max(maxover, speedict[segspeedlens[curspeedseg]] - limitdict[seglimitlens[curlimitseg]])

    fout.write(str(maxover))
speed()