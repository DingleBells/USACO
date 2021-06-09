def dilate(strings, factor):
    returnlist = []
    for line in strings:
        newline = ""
        for ch in line:
            newline += ch*factor
        returnlist += [newline]*factor
    return returnlist

def solve():
    fin = open("cowsignal.in")
    fout = open("cowsignal.out", "w")
    strings = []
    a,b,k = map(int, fin.readline().split())
    for line in fin.readlines():
        strings.append(line.strip())
    result = dilate(strings,k)
    for thing in result:
        fout.write(f"{thing}\n")

solve()