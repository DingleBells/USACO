def findsecondlargest(namelist, number, n):
    milkdict = {}
    for i in range(n):
        if namelist[i] in milkdict:
            milkdict[namelist[i]] += number[i]
        else:
            milkdict[namelist[i]] = number[i]
    milkdict = {k: v for k, v in sorted(milkdict.items(), key=lambda item: item[1])}
    print(milkdict, list(milkdict.values()))
    secsmallest = second_smallest(list(milkdict.values()))
    # print(secsmallest,list(milkdict.values()))
    one = False
    # print(milkdict)
    for key in milkdict:
        val = milkdict[key]
        if val == secsmallest:
            if not one:
                one = key
            else:
                return "Tie"
    return one



def second_smallest(numbers):
    if (len(numbers)<2):
        return
    if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
        return
    dup_items = set()
    uniq_items = []
    for x in numbers:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
            uniq_items.sort()
    return uniq_items[1]

def solve():
    fin = open("notlast.in")
    fout = open("notlast.out", 'w')
    n = int(fin.readline())
    namelist = []
    numlist = []
    for i in range(n):
        line = fin.readline().split()
        name,num = line[0], int(line[1])
        namelist.append(name)
        numlist.append(num)
    fout.write(f"{findsecondlargest(namelist, numlist, n)}")

print(second_smallest([4,4,4,4]))