def find(n, mailboxes):
    for l in range(1, n+1):
        sequences = set()
        for i in range(n- l + 1):
            sequences.add(mailboxes[i:i+l])
        if len(sequences) == (n-l + 1):
            ans = l
            return ans
    return n

def solve():
    fin = open("whereami.in")
    fout = open("whereami.out", 'w')
    n = int(fin.readline())
    boxes = fin.readline()
    fout.write(f"{find(n,boxes)}")

solve()