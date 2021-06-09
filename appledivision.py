def find(n,weights,i, s1,s2):
    if i == n:
        return abs(s1-s2)
    return min(find(n,weights,i+1, s1+weights[i], s2), find(n,weights,i+1, s1,s2+weights[i]))

def solve():
    n = int(input())
    weights = list(map(int, input().split()))
    print(find(n,weights,0,0,0))

solve()