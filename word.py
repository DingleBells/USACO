# for each word in the sentence
# find the length of the word
# if wordlen + linelen > k:
# put word on next line

def format(splitstring, k):
    outstring = ""
    linecounter = 0
    for word in splitstring:
        wordlen = len(word)
        if linecounter + wordlen > k:
            outstring += "\n"
            outstring += word
            linecounter = wordlen
        else:
            if linecounter != 0:
                outstring += " "
            outstring +=  word
            linecounter += wordlen
    return outstring

def solve():
    fin = open("word.in")
    fout = open("word.out", "w")
    a,k = map(int, fin.readline().split())
    wordlist = fin.readline().split()
    fout.write(f"{format(wordlist, k)}")

solve()