def sim(startshell, a,b,g,n):
    curShell = startshell
    correct = 0
    for i in range(n):
        if a[i] == curShell:
            curShell = b[i]
        elif b[i] == curShell:
            curShell = a[i]
        if curShell == g[i]:
            correct += 1
    return correct

def solve():
    fin = open("shell.in")
    fout= open("shell.out", "w")
    n = int(fin.readline())
    a,b,g = [],[],[]
    for w in range(n):
        x,y,z = map(int, fin.readline().split())
        a.append(x)
        b.append(y)
        g.append(z)
    fout.write(f"{max(sim(1,a,b,g,n),sim(2,a,b,g,n),sim(3,a,b,g,n))}")

solve()