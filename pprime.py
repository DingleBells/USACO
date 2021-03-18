"""
ID: kanghee2
LANG: PYTHON3
PROG: pprime
"""
import time
def generateEvenPalindromes(numDigits):
    numberList = []
    if numDigits == 2:
        return ['11','33','55','77','99']
    for firstDigit in ['1','3','5','7','9']:
        for num in range(0,10**int(((numDigits-2))/2)):
            stringNum = str(num).zfill(int(((numDigits-2))/2))
            halfNum = firstDigit + stringNum
            fullNum = halfNum+halfNum[::-1]
            numberList.append(fullNum)
    return numberList
# # for odd palindromes insert a number in the middle

primeDictionary = {}


def isPrime(n):
    # if n in primeDictionary:
    #     return primeDictionary[n]

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
            # primeDictionary[n] = False
            return False
        i = i + 6
    # primeDictionary[n] = True
    return True


# for odd palindromes insert a number in the middle

def generatePrimeOddPalindromes(numDigits):
    if numDigits == 1:
        return [5,7]
    evenPalindromes = generateEvenPalindromes(numDigits-1)
    mid = int((numDigits-1)/2)
    newPals = []
    for thing in evenPalindromes:
        for digit in ['0','1','2','3','4','5','6','7','8','9']:
            number = int(thing[:mid]+digit+thing[mid:])
            if isPrime(number):
                newPals.append(number)
    return newPals

def binarySearchForThing(searchingFor, lower, upper, entireList):
    mid = (lower+upper)//2
    # print(lower, upper)
    if lower > upper:
        return upper
    if lower == upper:
        if entireList[lower] > searchingFor:
            if lower != 0:
                return lower -1
            else:
                return 0
        else:
            return lower
    elif entireList[mid] == searchingFor:
        return mid
    elif entireList[mid] > searchingFor:
        newUpper = mid
        return binarySearchForThing(searchingFor, lower, newUpper-1, entireList)
    else:
        newLower = mid
        return binarySearchForThing(searchingFor, newLower+1, upper, entireList)

def generatePalindromesInRange(lower, upper):
    # start from the top and add to list
    palindromeList = []
    curNumDigits = len("%i"%upper)
    # print(curNumDigits)
    if upper != 100000000:
        if curNumDigits %2 == 0:
            curNumDigits -= 1
        largestPalindromes = generatePrimeOddPalindromes(curNumDigits)

        # print(largestPalindromes)
        # print(upper)
        cutIndex = binarySearchForThing(upper, 0, len(largestPalindromes) - 1, largestPalindromes)
        bottomCutIndex = binarySearchForThing(lower, 0, len(largestPalindromes)-1, largestPalindromes)
        # print(bottomCutIndex, cutIndex, largestPalindromes)
        if largestPalindromes[bottomCutIndex] < lower:
            bottomCutIndex += 1
        palindromeList += largestPalindromes[bottomCutIndex:cutIndex + 1]
    numDigitsInLower = len("%i"%lower)

    curNumDigits -= 1

    while curNumDigits > numDigitsInLower and curNumDigits >= 1:

        if curNumDigits % 2 == 0:
            pass
        else:

            palindromeList += generatePrimeOddPalindromes(curNumDigits)
        curNumDigits -= 1
    if 11 >= lower:
        palindromeList.append(11)

    if curNumDigits % 2 != 0:
        smallest = generatePrimeOddPalindromes(curNumDigits)
        cutIndex = binarySearchForThing(lower, 0, len(smallest) - 1, smallest)
        if smallest[cutIndex] < lower:
            cutIndex += 1
        palindromeList += smallest[cutIndex:]
    return palindromeList

def solvetheproblem():
    fin = open("pprime.in")
    fout = open("pprime.out", "w")
    lower, upper = map(int, fin.readline().split())
    pprimelist = sorted(generatePalindromesInRange(lower, upper))
    for number in pprimelist:
        fout.write(f"{number}\n")

# start = time.time()
solvetheproblem()
# end = time.time()
# print(end-start)
# only need to generate the