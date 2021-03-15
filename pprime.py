def generateEvenPalindromes(numDigits):
    numberList = []
    if numDigits == 2:
        return [11,33,55,77,99]
    if numDigits == 4:
        bottom = 0
    else:
        bottom = 10**(int(numDigits/2)-2)
    for firstDigit in ['1','3','5','7','9']:
        for num in range(bottom,10**(int(numDigits/2)-1)):
            # stringNum = str(num).zfill()
            stringNum = str(num)
            halfNum = firstDigit + stringNum
            fullNum = halfNum+halfNum[::-1]
            numberList.append(int(fullNum))
    return numberList
# # for odd palindromes insert a number in the middle

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


# for odd palindromes insert a number in the middle

def generatePrimeOddPalindromes(numDigits):
    if numDigits == 1:
        return [5,7]
    evenPalindromes = generateEvenPalindromes(numDigits-1)
    mid = int((numDigits-1)/2)
    newPals = []
    for thing in evenPalindromes:
        for digit in ['0','1','2','3','4','5','6','7','8','9']:
            thing = str(thing)
            number = int(thing[:mid]+digit+thing[mid:])
            if isPrime(number):
                newPals.append(number)
    return newPals

def binarySearchForThing(searchingFor, lower, upper, entireList):
    mid = int((lower+upper)/2)
    if lower == upper:
        if entireList[lower] > searchingFor:
            return lower -1
        else:
            return lower
    if entireList[mid] == searchingFor:
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
    if curNumDigits %2 == 0:
        curNumDigits -= 1
    largestPalindromes = generatePrimeOddPalindromes(curNumDigits)
    cutIndex = binarySearchForThing(upper, 0, len(largestPalindromes) - 1, largestPalindromes)
    palindromeList += largestPalindromes[:cutIndex + 1]
    numDigitsInLower = len("%i"%lower)
    curNumDigits -= 1
    while curNumDigits != numDigitsInLower:
        if curNumDigits % 2 == 0:
            pass
        else:
            palindromeList += generatePrimeOddPalindromes(curNumDigits)
        curNumDigits -= 1

    if curNumDigits %2 == 0:
        return palindromeList
    else:
        smallest = generatePrimeOddPalindromes(curNumDigits)
        cutIndex = binarySearchForThing(lower, 0, len(smallest) - 1, smallest)
        palindromeList += smallest[cutIndex:]
    return palindromeList

def solvetheproblem():
    fin = open("pprime.in")
    fout = open("pprime.out", "w")
    lower, upper = map(int, fin.readline().split())
    pprimelist = sorted(generatePalindromesInRange(lower, upper))
    for number in pprimelist:
        fout.write(f"{number}\n")


solvetheproblem()

# only need to generate the