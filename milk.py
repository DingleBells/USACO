"""
ID: kanghee2
LANG: PYTHON3
PROG: milk
"""
# create a function that will return the minimum price given a list sorted by price and the target bottles
def findBestPrice(sortedlist, target_bottles):
    finalprice = 0
    totalbottles = 0
    for (price, quantity) in sortedlist:
        if quantity + totalbottles >= target_bottles:
            finalprice += price*(target_bottles - totalbottles)
            return finalprice
        else:
            totalbottles += quantity
            finalprice += price*quantity
    return 0

def solveTheProblem():
    fin = open('milk.in')
    fout = open('milk.out', 'w')
    # get the number of bottles needed and a list sorted by best price
    line = fin.readline().split()
    bottlesneeded, farmers = int(line[0]), int(line[1])
    priceAndQuantList = []
    for line in fin.readlines():
        line = line.split()
        priceAndQuantList.append((int(line[0]), int(line[1])))
    priceAndQuantList.sort(key=lambda tup: tup[0])
    fout.write(f"{findBestPrice(priceAndQuantList, bottlesneeded)}\n")

solveTheProblem()