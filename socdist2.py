inp = open("socdist2.in").read().strip().split("\n")
n = int(inp[0])
inp.pop(0)
cows = list(map(lambda x: tuple(map(int, x.split(" "))), inp))
cows.sort()
r = 1000000000
infected = []
for i in range(n-1):
  if cows[i][1] != cows[i+1][1]:
    r = min(r, cows[i+1][0]-cows[i][0])

r-=1

count = 1
for i in range(n):
  if cows[i][1] == 1:
    if len(infected) > 0:
      if cows[i][0] - infected[-1] > r:
        count+=1
    infected.append(cows[i][0])

f = open("socdist2.out", "w")
f.write(str(count))
f.close()
