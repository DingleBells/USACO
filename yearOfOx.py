animals = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake",
           "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]

def get_animal(year):
    a = 0
    y = 2021
    while y < year:
        if a == 11:
            a = 0
        else:
            a += 1
        y+= 1
    while y > year:
        if a == 0:
            a = 11
        else:
            a -= 1
        y -= 1
    # print(a)
    return animals[a]

def solvetheproblem():
    when_born  = {}
    when_born["Bessie"] = 2021
    n = int(input())
    inputlist = []
    for i in range(n):
        inputlist.append(input())
    for i in range(n):
        [cowa, born, bornin, relation, animal, year, fromsomeone, cowb] = inputlist[i].split()
        when_born[cowa] = when_born[cowb]
        if get_animal(when_born[cowa]) == animal:
            if relation == "previous":
                when_born[cowa] -= 1
            else:
                when_born[cowa] += 1
        while (get_animal(when_born[cowa]) != animal):
            if relation == "previous":
                when_born[cowa] -= 1
            else:
                when_born[cowa] += 1
        # print(when_born)
    diff = abs(when_born["Bessie"]-when_born["Elsie"])
    print(f"{diff}")

solvetheproblem()