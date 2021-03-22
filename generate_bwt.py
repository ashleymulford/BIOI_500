
#read in file
file = open("/Users/ashle/Downloads/rosalind_ba9i.txt")

lines = []
for line in file:
    lines.append(line)

string = lines[0].strip("\n")

    
#string = "GCGTGCCTGGTCA$"

def get_bwt(string):
    #create list of all rotations of string:
    rotations = []
    #iterate through and get two strings split at index i
    for i in range(len(string)):
        string1 = string[0:i]
        string2 = string[i:len(string)]
        #join to get rotation of original
        string_rotation = string2 + string1
        #add to list
        rotations.append(string_rotation)
    #sort lexographically
    rotations.sort()
    bwt = ""
    #get bwt from last index of each string in list of rotations
    for item in rotations:
        bwt = bwt + item[len(item)-1]
    #return bwt
    return bwt


bwt = get_bwt(string)

#output to file
output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind10_answer.txt", "w")
output.write(bwt)
