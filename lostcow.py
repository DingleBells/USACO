def solve():
    fin = open("lostcow.in")
    fout = open('lostcow.out' ,'w')
    x,y = map(int, fin.readline().split())
    ans = 0
    by = 1
    di = 1
    while True:
        if (di == -1 and x-by <= y and y <= x) or (di == 1 and x<= y and y<=x+by):
            ans += abs(y-x)
            fout.write(str(ans))
            break
        else:
            ans += by*2
            by *= 2
            di *= -1


solve()
