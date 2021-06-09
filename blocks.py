
import sys

sys.stdin = open("blocks.in", 'r')
sys.stdout = open("blocks.out", 'w')
def countfreq(s):
    freqs = [0]*26
    for c in s:
        freqs[ord(c)-ord('a')] += 1
    return freqs

n = int(input())

ans = [0] * 26
#
# print(ans)

for i in range(n):
    s1, s2 = input().split()
    freq1, freq2 = countfreq(s1), countfreq(s2)
    # print(s1, freq1, s2, freq2)
    for j in range(26):
        ans[j] += max(freq1[j], freq2[j])

for i in ans:
    print(i)