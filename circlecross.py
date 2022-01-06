fin = open("circlecross.in")
fout = open("circlecross.out", 'w')
s = fin.readline().strip()

ans = 0

for a in range(52):
    for b in range(a+1, 52):
        for c in range(b+1, 52):
            for d in range(c+1, 52):
                ans += s[a] == s[c] and s[b] == s[d]

fout.write(str(ans))
