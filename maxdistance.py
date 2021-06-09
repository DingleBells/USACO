def dist(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

def find():
    n = int(input())
    xcoords = list(map(int, input().split()))
    ycoords = list(map(int, input().split()))
    largest = 0
    for i in range(n):
        for q in range(i+1,n):
            thing = dist(xcoords[i], ycoords[i], xcoords[q], ycoords[q])
            if thing > largest:
                largest=thing
    return largest

print(find())