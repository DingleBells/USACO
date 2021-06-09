"""
ID: kanghee2
LANG: PYTHON3
PROG: dualpal
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

def isPalindrome(innum):
    stringednum = str(innum)
    for pos, ch in enumerate(stringednum[:int(len(stringednum)/2) +1]):
        if ch != stringednum[len(stringednum)-1-pos]:
            return False
    return True

def baseEncode(base10num, base):
    digits = '01234567890'
    remstack = Stack()
    while base10num > 0:
        rem = base10num % base
        remstack.push(rem)
        base10num = base10num // base
    newstring = ''
    while not remstack.isEmpty():
        newstring += digits[remstack.pop()]
    return newstring

def solvetheproblem():
    fin = open("dualpal.in", 'r')
    fout = open("dualpal.out", 'w')
    [num1, num2] = fin.readline().strip().split()
    numlist = []
    while len(numlist) != int(num1):
        num2 = int(num2) +1
        timespalindrome = 0
        for base in range(2, 11):
            if isPalindrome(baseEncode(num2, base)):
                timespalindrome += 1
            if timespalindrome == 2:
                numlist.append(num2)
                break

    for item in numlist:
        fout.write(f"{item}\n")
    return

solvetheproblem()