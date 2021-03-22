'''
This script uses a burrows-wheeler transform and a list of patterns and outputs the number of times each pattern occurs in the original DNA sequence
'''



#open file and extract data
file = open("/Users/ashle/Downloads/rosalind_ba9l.txt")

line_list = []

for line in file:
    line_list.append(line.strip("\n"))

bwt = line_list[0]
pattern_list = line_list[1].split(" ")


#bwt = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
#pattern_list = ["CCT", "CAC", "GAG", "CAG", "ATC"]

#function to get first column as string from bwt
def get_first(bwt):
    bwt_list = []
    #iterate through string and add char to list
    for l in bwt:
        bwt_list.append(l)
    #sort list lexicographically
    bwt_list.sort()
    #concatenate to get string
    first = ''.join(bwt_list)
    return first

#function to generate dict to keep track of what base is at what position in string
#key are all bases plus $, values are lists of indices
def get_pos_dict(string):
    pos_dict = {}
    #iterate through string
    for i in range(len(string)):
        c = string[i]
        #if char not already a key, add with index as list
        if c not in pos_dict:
            pos_dict[c] = [i]
        #else update existing list with current index
        else:
            pos_dict[c].append(i)
    return(pos_dict)


#get index in first where base equals base at pos in bwt
def last_to_first(bwt, pos):
    #get first string
    first = get_first(bwt)
    #get position dicts for first and bwt
    bwt_pos_dict = get_pos_dict(bwt)
    first_pos_dict = get_pos_dict(first)
    #initialize key and index
    pos_key = ""
    key_index = 0
    #iterate through bwt position dict to find key with value list containing pos
    for key in bwt_pos_dict:
        pos_list = bwt_pos_dict[key]
        for i in range(len(pos_list)):
            #if pos in list save key and index
            if pos_list[i] == pos:
                pos_key = key
                key_index = i
    #get index from first pos dict using key (base) and value list index
    first_index = first_pos_dict[pos_key][key_index]
    return first_index


#check if a pattern in found in the original seq using bwt
def bwt_matching(bwt, pattern):
    #initialize pointers for full length of bwt
    top = 0
    bottom = len(bwt)-1
    #make sure top is pointing to index before bottom
    while top <= bottom:
        #if len of pattern greater than 0 must continue to check
        if len(pattern) != 0:
            #get base to check for, use last base since working backwards
            base = pattern[len(pattern)-1]
            #update pattern, remove current base
            pattern = pattern[:-1]
            #if base found within bwt between current pointers
            if base in bwt[top:bottom+1]:
                #get index of first occurrence
                top_index = bwt.find(base, top, bottom+1)
                #get index of last occurrence
                bottom_index = bwt.rfind(base, top, bottom+1)
                #get last to first for each indices and update pointers
                #this finds the corresponding indices from first column
                #these become new pointers for bwt, check preceeding base in following loop
                top = last_to_first(bwt, top_index)
                bottom = last_to_first(bwt, bottom_index)
            #if base not found in current subset of bwt
            #then pattern is not found in original seq
            else:
                return 0
        #if len of pattern 0 then full pattern checked, ready to output    
        else:
            return bottom - top + 1


string = ""

for pattern in pattern_list:
    string = string + str(bwt_matching(bwt, pattern)) + " "

print(string)


'''
#save answer in output file
output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind13_answer.txt", "w")

for pattern in pattern_list:
    output.write(str(bwt_matching(bwt, pattern)) + " ")

'''











