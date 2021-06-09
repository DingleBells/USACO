def tryall(x,y,m):
    smallest = 1001
    smallest = min(smallest, m-x*(m//x),m-y*( m//y))
    for i in range(int(m/x) + 1,0,-1):
        for q in range(int(m/y) + 1):
            cur = i*x +q*y
            if cur <= m:
                smallest = min(smallest, m-cur)
                if smallest == 0:
                    return m
    return m-smallest

def solve():
    fin = open("pails.in")
    fout = open("pails.out", "w")
    x,y,m = map(int, fin.readline().split())
    fout.write(f"{tryall(x,y,m)}")

solve()