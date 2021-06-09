def find(inlist):
    return len(set(inlist))

if __name__ == "__main__":
    x = input()
    numlist = list(map(int, input().split()))
    print(find(numlist))

