def angle_from_direction(a):
    if a == "E":
        return 0
    if a  == "N":
        return 90
    if a == "W":
        return 180
    if a == "S":
        return 270

def angle_change(a, b):
    thing1 = angle_from_direction(a)
    thing2 = angle_from_direction(b)
    if thing1 == thing2:
        return 0
    elif (thing2 == (thing1 + 90)%360):
        return 90
    elif (thing2 == (thing1 + 270)%360):
        return -90
    else:
        return False

def test(instring):
    totalChange = 0
    for index in range(len(instring)):
        totalChange += angle_change(instring[index], instring[(index+1)%(len(instring))])
    if totalChange == 360:
        return "CCW"
    else:
        return "CW"

def solveTheProblem():
    n = int(input())
    stringlist = []
    for x in range(n):
        stringlist.append(input())
    for string in stringlist:
        print(test(string))

solveTheProblem()