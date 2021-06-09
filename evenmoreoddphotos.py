n = int(input())
s = list(map(int, input().split()))

odds = 0
evens = 0
for num in s:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

def group(O,E):
    diff = O-E
    if diff == 0:
        return O+E
    elif diff == 1:
        return O+E-2
    elif diff == 2:
        return E+O-1
    else:
        O -= 2
        E += 1
        return group(O,E)

if evens > odds:
    print(2*odds + 1)
else:
    print(group(odds, evens))

