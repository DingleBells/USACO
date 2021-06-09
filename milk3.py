"""
ID: kanghee2
LANG: PYTHON3
PROG: milk3
"""

def simulatePours(cup_capacity, cup_state, cup_history, start, to):
    start_amount = cup_state[start]
    to_amount = cup_state[to]
    amountToPour = min(start_amount, cup_capacity[to] - to_amount )
    if amountToPour == 0:
        return
    new_cup_state = cup_state.copy()
    new_cup_state[start] -= amountToPour
    new_cup_state[to] += amountToPour

    new_cup_state_key = (new_cup_state['a'], new_cup_state['b'], new_cup_state['c'])
    if new_cup_state_key in cup_history:
        return

    cup_history.add(new_cup_state_key)

    for fromnode in 'abc':
        for toNode in 'abc':
            if fromnode != toNode:
                simulatePours(cup_capacity, new_cup_state, cup_history, fromnode, toNode)

def getFinalValues(cupSetHistory):
    returnset = set()
    for (a,b,c) in cupSetHistory:
        if a == 0:
            returnset.add(c)
    return returnset

def solveTheProblem():
    fin = open('milk3.in')
    fout = open('milk3.out', 'w')
    line = fin.readline().strip().split()
    a, b, c = int(line[0]), int(line[1]), int(line[2])

    cupCapacity = {'a': a, 'b': b, 'c': c}
    cupState = {'a': 0, 'b': 0, 'c': c}
    cupHistory = set([])
    cupHistory.add((cupState['a'], cupState['b'], cupState['c']))

    simulatePours(cupCapacity, cupState, cupHistory, 'c', 'a')
    simulatePours(cupCapacity, cupState, cupHistory, 'c', 'b')

    goodValues = sorted(list(getFinalValues(cupHistory)))

    outstring = " ".join(str(i) for i in goodValues)
    fout.write(f"{outstring}\n")
    return

solveTheProblem()