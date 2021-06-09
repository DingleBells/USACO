# first sort the input
people = int(input())
weights = list(map(int, input().split()))


weights.sort()

previous = -1
sum = 0
final = weights[-1]

for x in range(people):
    for y in range(people):
        previous = -1
        sum = 0
        for z in range(people):
            if z == x or z == y:
                continue
            if previous == -1:
                previous = weights[z]
            else:
                sum += weights[z]-previous
                previous = -1
        final = min(sum, final)


print(final)