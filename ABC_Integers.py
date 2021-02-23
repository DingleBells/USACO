def findABC(numList):
    # two smallest are A and B, C would be Largest - A-B
    # finding the two smallest
    numList = sorted(numList)
    smallest = numList[0]
    secondSmallest = numList[1]
    largest = numList[-1]
    return f"{smallest} {secondSmallest} {largest-smallest-secondSmallest}"
    # Largest = A + B + C

if __name__ == "__main__":
    numList = list(map(int, input().split()))
    print(findABC(numList))
