def solve():
    fin = open("herding.in")
    fout = open("herding.out", 'w')
    a,b,c = map(int, fin.readline().split())
    if a > b:
        temp  =a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    if a > b:
        temp = a
        a = b
        b = temp

    if c == a+2:
        fout.write("0\n")
    elif b == a+2 or c == b+2:
        fout.write("1\n")
    else:
        fout.write("2\n")
    fout.write(f"{max(b-a, c-b) -1}")

solve()