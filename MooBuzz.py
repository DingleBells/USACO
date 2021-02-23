# iterate through the numbers one by one


def mooBuzz(n):
    x = 1
    while n != 1:
        x += 1
        if not(x % 5 ==0 or x % 3 == 0):
            n -= 1
    return x

if __name__ == "__main__":
    fin = open("moobuzz.in")
    fout = open("moobuzz.out", "w")
    n = int(fin.readline())
    fout.write(str(mooBuzz(n)))