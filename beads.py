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
len_necklace = int(len_necklace)
beads_max = 0
necklace = necklace.rstrip()
def _IsColorCompatible(segment_color, current_bead):
    return segment_color == 'w' or current_bead == 'w' or segment_color == current_bead
for pos, letter in enumerate(necklace):
    forward_counter = 0
    backwardcounter = 0
    segment_color = necklace[pos]
    newnecklace = list(necklace)
    # finding string going forward and compare current bead to starting bead
    for index in range(len_necklace):
        current_bead = newnecklace[(pos + index) % len_necklace]
        if _IsColorCompatible(segment_color, current_bead):
            forward_counter += 1
            newnecklace[index] = 'x'
            if current_bead != 'w':
                segment_color = current_bead
        else:
            break
    starting_bead2 = newnecklace[pos-1]
    # find string going backward and compare to first bead
    segment_color2 = necklace[pos-1]
    for reverse_index in range(len_necklace, 0, -1):
        backwards_bead = newnecklace[(pos + reverse_index - 1) % len_necklace]
        if backwards_bead == 'x':
            break
        if _IsColorCompatible(segment_color, backwards_bead):
            backwardcounter += 1
        else:
            break
    if (forward_counter+backwardcounter) > beads_max:
        beads_max = forward_counter+backwardcounter

fout.write(f"{beads_max}\n")
