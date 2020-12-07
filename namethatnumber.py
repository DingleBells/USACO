"""
ID: kanghee2
LANG: PYTHON3
PROG: namenum
"""
def solveTheProblem():
    fin = open('namenum.in', 'r')
    fout = open('namenum.out', 'w')
    dictfile = open('dict.txt', 'r')
    numToLetter = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'],
                   7: ['P', 'R', 'S'],
                   8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y']}

    namedict = {}
    for name in dictfile.readlines():
        namedict[name.strip()] = None
    number = int(fin.readline().strip())

    lists = []

    for digit in f"{number}":
        lists.append(numToLetter[int(digit)])

    def generateWordList(toplist, namedict, prefix):

        if len(toplist) == 0:
            if prefix in namedict:
                return [prefix]
            else:
                return []
        else:
            wordlist = []
            for letter in toplist[0]:
                newprefix = prefix
                newprefix += letter
                wordlist += (generateWordList(toplist[1:], namedict, newprefix))
            return wordlist

    my_wordlist = generateWordList(lists, namedict, '')
    my_wordlist.sort()
    if my_wordlist == []:
        fout.write("NONE\n")
    else:
        for item in my_wordlist:
            fout.write(f"{item}\n")

solveTheProblem()