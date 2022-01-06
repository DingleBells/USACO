fin = open("paint.in")
fout = open("paint.out", 'w')

a,b = map(int, fin.readline().split())
c,d= map(int, fin.readline().split())
cover = [0] * 100
for i in range(a, b):
    cover[i] = 1
for i in range(c, d):
    cover[i] = 1
ans = 0
for i in range(100):
    ans += cover[i]
fout.write(str(ans))