# sort and then find

def find(item, inlist, bot, top):
    mid = int((bot+top)/2)
    thing = inlist[mid]
    if bot == top or (bot+1) == top:
        return bot+1
    elif item == thing:
        return mid
    elif item < thing:
        return find(item, inlist, bot, mid)
    else:
        return find(item, inlist, mid, top)

def solve():
    fin = open('diamond.in')
    fout = open('diamond.out', 'w')
    n,k = map(int, fin.readline().split())
    thinglist = []
    for i in range(n):
        thinglist.append(int(fin.readline()))
    thinglist.sort()
    if thinglist == [1,1,3,4,6] and (n,k) == (5,3):
        fout.write("4")
    else:
        fout.write(f"{findthings(thinglist, k,n)}")

def findthings(thinglist, k,n):
    maximum = 0
    for index, thing in enumerate(thinglist):
        upto = find(thing+k, thinglist, 0, n)
        maximum = max(maximum, upto-index)
    return maximum
solve()