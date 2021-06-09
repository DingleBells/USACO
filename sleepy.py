fin = open('sleepy.in')
n = int(fin.readline())
cows = list(map(int, fin.readline().split()))
ans = 0

for i in range(n-1, 0,-1):
    if cows[i] < cows[i-1]:
        ans = i
        break

fout = open("sleepy.out", 'w')
fout.write(str(ans))

