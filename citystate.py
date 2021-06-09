# append the states and the cities to a set
# for each city contraction see if a state exists
# if it does, add (city, state) pair to another set
# return length of the set


def solve():
    fin = open("citystate.in")
    fout = open("citystate.out", 'w')
    n = int(fin.readline())
    citystate = set()
    counter = 0
    for i in range(n):
        city, state = fin.readline().split()
        thing = city[:2] + state
        citystate.add(thing)
    things = set()
    for thing in citystate:
        if thing[2:] + thing[:2] in citystate:
            print(thing, thing[2:] + thing[:2])
            things.add(tuple(sorted((thing, thing[2:] + thing[:2]))))
    print(citystate)
    fout.write(str(len(things)))

solve()