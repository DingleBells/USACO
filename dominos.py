n,m,k = map(int, input().split())

rows = []

things = []
for i in range(n):
    things.append(input().split())

# print(things)

for nums in things:
    maxinthisrow = 0
    curmax = 0
    for num in nums:
        if num == "1":
            curmax += 1
        elif num == "0":
            maxinthisrow = max(curmax, maxinthisrow)
            curmax = 0

    maxinthisrow = max(curmax, maxinthisrow)
    # print(curmax, maxinthisrow)
    rows.append(maxinthisrow)

# print(rows)
rows.sort(reverse=True)
print(sum(rows[:k]))