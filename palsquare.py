"""
ID: kanghee2
LANG: PYTHON3
PROG: palsquare
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
# Start with the easy stuff:
# Make function to check if a number is a palindrome by comparing the last num to the first num and so on

def isPalindrome(innum):
    stringednum = str(innum)
    for pos, ch in enumerate(stringednum[:int(len(stringednum)/2) +1]):
        if ch != stringednum[len(stringednum)-1-pos]:
            return False
    return True

# Functions to encode to base n and decode from base n
def baseEncoder(base10num, n):
    digits = '0123456789ABCDEFGHIJ'
    remstack = Stack()

    while base10num > 0:
        rem = base10num % n
        remstack.push(rem)
        base10num = base10num // n

    newString = ''
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]
    return newString

def baseDecoder(baseN_num, n):
    digits = '0123456789ABCDEFGHIJ'
    digitlist = []
    for ch in baseN_num:
        digitlist.append(ch)
    exponentcounter = 0
    final = 0
    while digitlist:
        lastdigit = digitlist.pop()
        index = digits.index(lastdigit)
        final += index * (n**exponentcounter)
        exponentcounter += 1
    return final

#final

def solveTheProblem():
    fin = open('palsquare.in', 'r')
    fout = open('palsquare.out', 'w')
    base = int(fin.readline().strip())
    mylist = []
    for number in range(1,301):
        num_squared_in_base_n = baseEncoder(number **2, base)
        if isPalindrome(num_squared_in_base_n):
            mylist.append((baseEncoder(number, base), num_squared_in_base_n))
    if mylist == []:
        fout.write('NONE\n')
    else:
        for (number, numsquared) in mylist:
            fout.write(f"{number} {numsquared}\n")
    return

solveTheProblem()