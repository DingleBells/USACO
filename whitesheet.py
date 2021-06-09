

def solve():
    x1,y1,x2,y2 = map(int, input().split())
    x3,y3,x4,y4 = map(int, input().split())
    x5,y5,x6,y6 = map(int, input().split())
    if (x3 <= x1 and x2 <= x4 and not(y4 <= y1 or y3 >= y2)):
        if y3 <= y1:
            y1 = y4 + 0.1
        elif y4 >= y2:
            y2 = y3-0.1
    if y3 <= y1 and y4 >= y2 and not(x4 <= x1 or x3 >= x2):
        if x3<=x1:
            x1 = x4 + 0.1
        elif (x4 >= x2):
            x2 = x3-0.1
    if x5 <= x1 and x6 >= x2 and not(y6 <= y1 or y5 >= y2):
        if y5 <= y1:
            y1 = y6 + 0.1
        elif y6 >= y2:
            y2 = y5 -0.1
    if y5 <= y1 and y6 >= y2 and not(x6 <= x1 or x5 >= x2)    :
        if x5 <= x1:
            x1 = x6 + 0.1
        elif x6 >= x2:
            x2 = x5-0.1
    if x1 > x2 or y1 > y2:
        print("NO")
    else:
        print("YES")

solve()