coinlist = [1 for x in range(int(input().split()[0]))]
for [a,b] in input().split():
    print(a,b)
    for i in range(int(a),int(b)):
        coinlist[i] *= -1
counter = 0
for coin in coinlist:
    if coin == -1:
        counter += 1
print(counter)