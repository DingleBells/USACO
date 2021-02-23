# make a function to find every permutation

# make another function to find whether there is an average flower in a permutation and count

def findPermutations(listLen):
    permList = []
    for x in range(listLen):
        for y in range(x, listLen):
            permList.append((x,y))
    return permList

def findAverageFlowers(flowerList):
    flowerPermutations = findPermutations(len(flowerList))
    averageCount = 0
    for permutation in flowerPermutations:
        (i,j) = permutation
        lookingAt = flowerList[i:j+1]
        averageFlower = sum(lookingAt)/((j-i)+1)
        # print(f"permutation: {permutation}, lookingAt: {lookingAt}, averageFlower: {averageFlower}")
        if averageFlower in lookingAt:
            averageCount += 1
    return averageCount

if __name__ == "__main__":
    input()
    flowers = list(map(int, input().split()))
    print(findAverageFlowers(flowers))