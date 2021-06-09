# def permutations(remaining, permset, candidate=""):
#     if len(remaining) == 0:
#         permset.add(candidate)
#         return
#     for i in range(len(remaining)):
#         newcandidate=  candidate + remaining[i]
#         newremaining = remaining[0:i] + remaining[i+1:]
#         permutations(newremaining,permset, newcandidate)
#     return permset

# instring = input()
# thing = sorted(list(permutations(instring, set())))
#
# print(len(thing))
# for i in thing:
#     print(i)

def permutations(self, remaining, permset, candidate=""):
    if len(remaining) == 0:
        permset.add(candidate)
        return
    for i in range(len(remaining)):
        newcandidate=  candidate + remaining[i]
        newremaining = remaining[0:i] + remaining[i+1:]
        permutations(newremaining,permset, newcandidate)
    return permset

def reorganizeString(self, S: str) -> str:
    total = list(permutations(S, set()))
    for string in total:
        prevch = string[0]
        repeated = False
        for ch in string[1:]:
            if ch == prevch:
                repeated = True
                break
            prevch = ch
        if not repeated:
            return string
    return ""

print(reorganizeString('aab'))


