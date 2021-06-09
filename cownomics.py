fin = open("cownomics.in")
fout = open("cownomics.out",'w')
a,b = map(int, fin.readline().split())
# open the file and read the genes in

# write down the genes of the spotty and non-spotty cows
spotty_cows = []
plain_cows = []
for i in range(a):
    spotty_cows.append(fin.readline())

for i in range(a):
    plain_cows.append(fin.readline())

# test all the positions
positions = []
for index in range(b): # loop through each possible index from 0-b
    # find what the spotty and plain cows have in their genes in that index
    spots = []
    for spotty in spotty_cows:
        spots.append(spotty[index])
    plains = []
    for plain in plain_cows:
        plains.append(plain[index])
    # start by assuming that the position is unique to the spotty cows
    # this can be proved wrong if there is a letter in the spotty cows' genes that
    # is also in the plain cows' genes

    isPossible = True
    for spot in spots:
        if spot in plains:
            isPossible =False
            break
    # if the spotty cows' genes are unique, append the index to a list
    if isPossible:
        positions.append(index)
# write the result out to the output file
fout.write(str(len(positions)))