"""
ID: kanghee2
LANG: PYTHON3
PROG: sprime
"""
# idea for solving the problem
# start with one digit in [2,3,5,7]
# add a digit to the end and check if prime
# if on the last digit, only use the odd numbers to check

def isPrime(n):

    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):

        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def findSuperprime(numDigits):
    curNumDigits = 1
    headers = [2,3,5,7]
    while curNumDigits < numDigits:
        newHeaders = []
        for header in headers:
            for digit in range(10):
                if isPrime(header*10 + digit):
                    newHeaders.append(header*10 + digit)
        curNumDigits += 1
        headers = newHeaders
    return headers

def solvetheproblem():
    fin = open("sprime.in")
    fout = open("8.sprime.out", "w")
    x  = int(fin.readline())
    sprimes = findSuperprime(x)
    for num in sprimes:
        fout.write(f"{num}\n")
solvetheproblem()