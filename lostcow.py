def solve():
    fin = open("lostcow.in")
    fout = open('lostcow.out' ,'w')
    x,y = map(int, fin.readline().split())

    ans = 0
    by = 1
    dir = 1
    while True:
        if dir == 1 and x <= y and y<= x+by:
            ans += abs(y-x)
            fout.write(str(ans))
            return
        else:
            ans += by*2
            by *= 2
            dir *= -1

solve()
