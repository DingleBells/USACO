def censor(string, stringtocensor):
    endstring = ""
    length = len(stringtocensor)
    for ch in string:
        endstring += ch
        if endstring.endswith(stringtocensor):
            endstring = endstring[:-length]
    return endstring

def solve():
    fin = open("censor.in")
    fout = open("censor.out", "w")
    s = fin.readline().strip()
    c = fin.readline().strip()
    fout.write(f"{censor(s,c)}")

solve()
