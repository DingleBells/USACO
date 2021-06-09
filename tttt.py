# idea for solving the problem
# make function to find all the possible ways to win(diagonal, horizontal, etc)
# with those values
# first check individual
# if there is a repeated string of one character, append to the single set
# second check team
# if there is a string with two of one kind and one of another, append to the doubleset
# return the length of the singleset
# return the length of the doubleset

fin = open("tttt.in")
fout = open("tttt.out", 'w')
inarr = []
for line in fin.readlines():
    inarr.append(line.strip())

def findWaysToWin(inarray):
    # easiest are the horizontals
    l1, l2, l3 = list(inarray[0]), list(inarray[1]), list(inarray[2])
    outlist = [l1,l2,l3]
    # verticals
    cur = []
    for i in range(3):
        cur = []
        for horizontal in inarray:
            cur.append(horizontal[i])
        outlist.append(cur)
    # diagonals
    # two cases {h1[1], h2[2], h2[3]}, {h1[3], h2[2], h3[1]}
    outlist.append([l1[0], l2[1], l3[2]])
    outlist.append([l1[2], l2[1], l3[0]])
    return outlist

def findsolutions(combinations):
    singles = set()
    doubles = set()
    for combination in combinations:
        thing = set(combination)
        # print(thing)
        if len(thing) == 1:
            singles.add(tuple(sorted(tuple(thing))))
        elif len(thing) == 2:
            # print(thing,sorted(tuple(thing)))
            doubles.add(tuple(sorted(tuple(thing))))
    # print("doubles", doubles)
    return len(singles), len(doubles)

waystowin = findWaysToWin(inarr)
# print(waystowin)
single, double = findsolutions(waystowin)
fout.write(f"{single}\n{double}")


