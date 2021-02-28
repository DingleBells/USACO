# more left turns = ccw
# more right turns = cw
import fileinput
# count the number of left or right turns
def determineLeftOrRight(facing, turn): # true if left, false if right
    if facing == turn:
        return None
    if facing == "N":
        if turn == "W":
            return True
        return False
    if facing == "S":
        if turn == "W":
            return False
        return True
    if facing == "E":
        if turn == "N":
            return True
        return False
    if facing == "W":
        if turn == "N":
            return True
        return False

def determineDirection(turnstring):
    currentDirection = turnstring[0]
    leftCount = 0
    for turn in turnstring[1:]:
        direction = determineLeftOrRight(currentDirection, turn)
        if direction != None:
            if direction:
                leftCount += 1
            else:
                leftCount -= 1
        # print(currentDirection, turn, f"Turned left?:{direction}", leftCount)
        currentDirection = turn
    if leftCount <= 0:
        print("CW")
    else:
        print("CCW")

def newDetermineDirection(start, end):
    if start == "N":
        if end == "E":
            return "CW"
        return "CCW"
    elif start == "S":
        if end == "E":
            return "CCW"
        return "CW"
    elif start == "E":
        if end == "N":
            return "CW"
        return "CCW"
    else:
        if end == "N":
            return "CCW"
        return "CW"
# def determineLast(instring):
#     reverseString = instring[::-1]
#     lastDirection = reverseString[0]
#     for letter in reverseString:
#         if lastDirection != letter:
#             secondToLast = letter
#             break
#     print(newDetermineDirection(secondToLast, lastDirection))


if __name__ == "__main__":
    inlines = []
    for line in fileinput.input():
        inlines.append(line)
    for thing in inlines[1:]:
        determineDirection(thing)