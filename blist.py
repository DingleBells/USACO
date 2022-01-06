def approach1():
    fin = open('blist.in')
    fout = open('blist.out', 'w')

    n = int(fin.readline().strip())
    cowlist = []
    for i in range(n):
        start, end, buckets = map(int, fin.readline().split())
        cowlist.append((start, end, buckets))
    cowlist.sort()

    maxBuckets = cowlist[0][2]
    for i in range(1,1001):
        buckets = 0
        for j in range(n):
            if i >= cowlist[j][0] and i <= cowlist[j][1]:
                buckets += cowlist[j][2]
        maxBuckets = max(buckets, maxBuckets)

    fout.write(str(maxBuckets))
approach1()
def approach2():
    fin = open('blist.in')
    fout = open('blist.out', 'w')

    n = int(fin.readline().strip())
    S = [0]*101
    T = [0]*101
    B = [0]*101
    start = [0]*1001
    finish = [0]*1001

    def solve(): # helper function for the logic of the problem
        bucketsNeeded = 0
        b = 0
        for t in range(1,1001):
            if start[t]:
                b += B[start[t]]
            bucketsNeeded = max(bucketsNeeded, b)
            if finish[t]:
                b-=B[finish[t]]
        return bucketsNeeded

    for i in range(n):
        s,f,b = map(int, fin.readline().split())
        S[i] = s
        T[i] = f
        B[i] = b
        start[S[i]] = i
        finish[T[i]] = i

    fout.write(str(solve()))
