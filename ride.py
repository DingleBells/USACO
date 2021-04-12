"""
ID: kanghee2
LANG: PYTHON3
PROG: ride
"""
ridein = open('ride.in', 'r')
rideout = open('ride.out','w')
alien, group = map(str, ridein.readlines())
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
alienlist = []
grouplist = []
for letter in alien.rstrip():
    alienlist.append(alphabet[letter.lower()])
for letter in group.rstrip():
    grouplist.append(alphabet[letter.lower()])

aliens = 1
groupnum = 1
for num in alienlist:
    aliens *= num
for num in grouplist:
    groupnum *= num
if groupnum %47 == aliens % 47:
    rideout.write('GO\n')
else:
    rideout.write('STAY\n')