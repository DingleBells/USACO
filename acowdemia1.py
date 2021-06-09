# idea for solving the problem
# first make a function that will calculate the h index
# then for i in range N:
# find the current h index
# add one to the current to find the next h index
# make a list with the papers that are below the next h index
# find the paper with the most citations that is below the next h index
# add one to it
def findLargest(papers, maxCit, length):
    curH = 0
    papers.sort(reverse=True)
    cited = set()
    done = False
    while not done:
        maybe = curH +1


        if maybe > length:
            done=True

        elif papers[maybe-1] < maybe:
            for x in range(maybe):
                # print(x)
                if papers[x] < maybe:
                    # print(papers[x], maybe, 1, maxCit)
                    if x in cited:
                        done = True
                        maybe -= 1

                        break
                    if 1 > maxCit:
                        done = True
                        break
                    else:
                        if x not in cited:
                            papers[x] += 1
                            maxCit -= 1
                            cited.add(x)
                            if papers[x] < maybe:
                                done = True
                                break

        if not done:
            curH = maybe
    # print(papers)
    return curH

def solvetheproblem():
    numPapers, maxCit = map(int, input().split())
    papers = list(map(int, input().split()))
    result = findLargest(papers, maxCit, numPapers)
    print(result)

solvetheproblem()
