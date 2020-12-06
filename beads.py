"""
ID: kanghee2
LANG: PYTHON3
PROG: beads
"""

#STEPS
#read file and get necklace, length
#make function that will return the string going forward from an index and going backward
#use that function in a for loop that will take every possible breaking point of the string
#the function will return the forward and backward, and find how long the color lasts for
#write output into a file
def FindMaxBeadLen(necklace):
    def _IsColorCompatible(segment_color, current_bead):
        return segment_color == 'w' or current_bead == 'w' or segment_color == current_bead

    len_necklace = len(necklace)
    beads_max = 0
    for pos, letter in enumerate(necklace):
        forward_counter = 0
        backwardcounter = 0
        segment_color = necklace[pos]
        newnecklace = list(necklace)
        # finding string going forward and compare current bead to starting bead
        for index in range(len_necklace):
            current_index= (pos + index) % len_necklace
            current_bead = newnecklace[current_index]
            if _IsColorCompatible(segment_color, current_bead):
                forward_counter += 1
                newnecklace[current_index] = 'x'
                if current_bead != 'w':
                    segment_color = current_bead
            else:
                break
        # find string going backward and compare to first bead
        segment_color2 = necklace[pos - 1]
        for reverse_index in range(len_necklace, 0, -1):
            backwards_bead = newnecklace[(pos + reverse_index - 1) % len_necklace]
            if backwards_bead == 'x':
                break
            if _IsColorCompatible(segment_color2, backwards_bead):
                backwardcounter += 1
                if backwards_bead != 'w':
                    segment_color2 = backwards_bead
            else:
                break
        if (forward_counter + backwardcounter) > beads_max:
            beads_max = forward_counter + backwardcounter
    return beads_max

# fin = open('beads.in', 'r')
# fout = open('beads.out', 'w')
# len_necklace, necklace = map(str,fin)
# beads_max = FindMaxBeadLen(necklace.strip())
# fout.write(f"{beads_max}\n")
#
#
print(FindMaxBeadLen('wwwbbrwrbrbrrbrbrwrwwrbwrwrrb'))
