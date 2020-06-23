"""
ID: kanghee2
LANG: PYTHON3
PROG: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
len_necklace, necklace = map(str,fin)
#STEPS
#read file and get necklace, length
#make function that will return the string going forward from an index and going backward
#use that function in a for loop that will take every possible breaking point of the string
#the function will return the forward and backward, and find how long the color lasts for
#write output into a file
max = 0
necklace = necklace.rstrip()
for pos, letter in enumerate(necklace):
    forward_counter = 0
    backwardcounter = 0
    starting_bead1 = necklace[pos]
    newnecklace = list(necklace)
    # finding string going forward and compare current bead to starting bead
    for index in range(len(newnecklace)):
        current_bead = necklace[(pos + index) % len(newnecklace)]
        if starting_bead1== 'w':
            starting_bead1 = current_bead
        if current_bead == starting_bead1 or current_bead == 'w':
            forward_counter += 1
            newnecklace[(pos + index) % len(newnecklace)] = 'x'
        else:
            break
    starting_bead2 = newnecklace[pos-1]
    # find string going backward and compare to first bead
    for reverse_index in range(len(newnecklace), 0, -1):
        backwards_bead = newnecklace[(pos + reverse_index - 1) % len(newnecklace)]
        if starting_bead2 == 'w':
            starting_bead2 = backwards_bead
        if backwards_bead == 'x':
            break
        if backwards_bead == starting_bead2 or backwards_bead == 'w':
            backwardcounter += 1
        else:
            break
    if (forward_counter+backwardcounter) > max:
        max = forward_counter+backwardcounter

fout.write(f"{max}\n")
