"""
ID: kanghee2
LANG: PYTHON3
PROG: gift1
"""
moneylist = open('gift1.in', 'r')
out = open('gift1.out', 'w')
peopledict = {}
num_persons = int(moneylist.readline())
file_lines = moneylist.readlines()
for position, line in enumerate(file_lines):
    if position < num_persons:
        peopledict[line.rstrip()] = 0
previousLine = ''
for position,line in enumerate(file_lines):
        if line.split()[0].isnumeric():
            givingmoneyto = []
            amount, peoplesharing = map(str, line.split(' '))
            person_sharing = previousLine.rstrip()
            if int(amount.rstrip()) != 0:
                peopledict[person_sharing] -= (int(amount)//int(peoplesharing))*int(peoplesharing)
            for index in range(int(position)+1, int(position)+1+int(peoplesharing)):
                givingmoneyto.append(file_lines[index].rstrip())
            for receiving in givingmoneyto:
                peopledict[receiving] += int(amount)//int(peoplesharing)
        previousLine = line

for position,person in enumerate(list(peopledict.keys())):
    out.write(f"{person} {list(peopledict.values())[position]}\n")