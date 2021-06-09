def numcommon(i,j, clist):
    count = 0
    v1 = clist[i]
    v2 = clist[j]
    for i in range(len(v1)):
        for j in range(len(v2)):
            if v1[i] == v2[j]:
                count += 1
    return count

def solve():
    fin = open("guess.in")
    fout= open("guess.out", 'w')
    n = int(fin.readline())
    characteristics = []
    for line in fin.readlines():
        split = line.split()
        characteristics.append([])
        for thing in split[2:]:
            characteristics[-1].append(thing)
    largest= 0
    for i in range(n):
        for j in range(i+1, n):
            largest = max(largest ,numcommon(i,j,characteristics))
    fout.write(f"{largest+1}\n")

solve()