class bucket:
    def __init__(self, maxcap, curcap):
        self.max = maxcap
        self.cur = curcap

def pour(start, end):
    amt = min(start.cur, end.max - end.cur)
    start.cur -= amt
    end.cur += amt

def solve():
    fin = open("mixmilk.in")
    fout = open("mixmilk.out", "w")
    a,b = map(int, fin.readline().split())
    b1 = bucket(a,b)
    c,d = map(int, fin.readline().split())
    b2 = bucket(c,d)
    e,f = map(int, fin.readline().split())
    b3 = bucket(e,f)
    for i in range(33):
        pour(b1,b2)
        pour(b2,b3)
        pour(b3,b1)
    pour(b1,b2)
    fout.write(f"{b1.cur}\n{b2.cur}\n{b3.cur}")
solve()